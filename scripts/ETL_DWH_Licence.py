"""_summary_
"""

import pandas as pd
import numpy as np
import json
from django.db.models import Q
from app.models import ODS_Licence
from app.models import D_Geography, D_Federation, D_Age_Group, D_Sexe, D_Date
from app.models import F_Licence
from rugby.settings import MAPPING_DIR


# Extract

d_geography_mapping = open(f"{MAPPING_DIR}/d_geography_mapping.json", 'rb').read()
d_geography_mapping = json.loads(d_geography_mapping)

d_federation_mapping = open(f"{MAPPING_DIR}/d_federation_mapping.json", 'rb').read()
d_federation_mapping = json.loads(d_federation_mapping)

d_date_mapping = open(f"{MAPPING_DIR}/d_date_mapping.json", 'rb').read()
d_date_mapping = json.loads(d_date_mapping)

d_age_group_mapping = open(f"{MAPPING_DIR}/d_age_group_mapping.json", 'rb').read()
d_age_group_mapping = json.loads(d_age_group_mapping)

d_sexe_mapping = open(f"{MAPPING_DIR}/d_sexe_mapping.json", 'rb').read()
d_sexe_mapping = json.loads(d_sexe_mapping)

f_licence_mapping = open(f"{MAPPING_DIR}/f_licence_mapping.json", 'rb').read()
f_licence_mapping = json.loads(f_licence_mapping)

queryset = ODS_Licence.objects.filter(Q(region="Auvergne-Rhône-Alpes"))

def run():
    
    #### D_GEOGRAPHY
    
    # Extract
    ods_columns = d_geography_mapping.keys()
    dwh_columns = d_geography_mapping.values()
    queryset_d_geography = queryset.values_list(*ods_columns).distinct()
    queryset_d_geography = list(queryset_d_geography)
    data = pd.DataFrame(queryset_d_geography, columns=dwh_columns)
    
    # Transform
    data['code'] = data['code_commune'] + '-' + data['code_qpv']
    data['departement'] = ''
    
    # Loading
    pk_d_geography = data['code']
    data = data.to_dict(orient='records')
    instance_d_geography = [D_Geography.objects.get_or_create(**row)[0] for row in data]
    

    #### D_FEDERATION

    # Extract
    ods_columns = d_federation_mapping.keys()
    dwh_columns = d_federation_mapping.values()
    queryset_d_federation = queryset.values_list(*ods_columns).distinct()
    queryset_d_federation = list(queryset_d_federation)
    data = pd.DataFrame(queryset_d_federation, columns=dwh_columns)
    
    # Transform
    
    # Loading
    pk_d_federation = data['code']
    data = data.to_dict(orient='records')
    instance_d_federation = [D_Federation.objects.get_or_create(**row)[0] for row in data]


    #### AGE GROUP
    
    # Transform
    data = {
        'code': d_age_group_mapping.keys(),
        'label': d_age_group_mapping.values()
    }
    
    data = pd.DataFrame(data)
    
    # Loading
    pk_d_age_group = data['code']
    data = data.to_dict(orient='records')
    instance_d_age_group = [D_Age_Group.objects.get_or_create(**row)[0] for row in data]



    #### SEXE
    
    # Transform
    data = {
        'code': d_sexe_mapping.keys(),
        'label': d_sexe_mapping.values()
    }
    
    data = pd.DataFrame(data)
    
    # Loading
    pk_d_sexe = data['code']
    data = data.to_dict(orient='records')
    instance_d_sexe = [D_Sexe.objects.get_or_create(**row)[0] for row in data]
    
    
    #### D_DATE
    
    # Extract
    ods_columns = d_date_mapping.keys()
    dwh_columns = d_date_mapping.values()
    queryset_d_date = queryset.values_list(*ods_columns).distinct()
    queryset_d_date = list(queryset_d_date)
    data = pd.DataFrame(queryset_d_date, columns=dwh_columns)
    
    # Transform
    data['year'] = data['date'].str.extract(r"(\d{4})")
    data['date'] = pd.to_datetime(data['year'])
    data['year'] = data['year'].astype(int)
    
    ETL_date = data['date'].to_list()[0]
    
    # Loading
    pk_d_date = data['date']
    data = data.to_dict(orient='records')
    instance_d_date = [D_Date.objects.get_or_create(**row)[0] for row in data]
    
    
    #### F_LICENCE
    
    F_Licence.objects.filter(Q(date_fk=ETL_date)).delete()
    
    # Extract
    ods_columns = f_licence_mapping.keys()
    dwh_columns = f_licence_mapping.values()
    queryset_f_licence = queryset.values_list(*ods_columns)
    queryset_f_licence = list(queryset_f_licence)
    data = pd.DataFrame(queryset_f_licence, columns=dwh_columns)
    
    # Transform
    values_columns = [column for column in data.columns if 'f_' in column or 'h_' in column]
    fk_columns = set(data.columns) - set(values_columns)
    data = data.melt(fk_columns, var_name='sexe-age', value_name='nombre')
    
    mask = data['nombre'] != '0'
    data = data.loc[mask]
    
    data['geography_fk'] = data['geography_fk'] + '-' + data['code_qpv']
    data = data.drop('code_qpv', axis=1)

    data['sexe_fk'] = data['sexe-age'].apply(lambda row: row[0].upper())
    
    data['age_group_fk'] = data['sexe-age'].str.extract(r"^[hf]_(\d{1,2}_\d{1,2})")
    data = data.drop('sexe-age', axis=1)
    
    data['date_fk'] = data['file_name'].str.extract(r"(\d{4})")

    data['code'] = data['geography_fk'] + '-' + data['federation_fk'] + '-' + data['age_group_fk'] + '-' + data['sexe_fk'] + '-' + data['date_fk']
    
    data['date_fk'] = pd.to_datetime(data['date_fk'])
    data = data.drop('file_name', axis=1)


    ### Instance Lookup
    
    dimension_table = {'geography_fk': pk_d_geography, 'instance': instance_d_geography}
    dimension_table = pd.DataFrame(dimension_table)
    data = pd.merge(data, dimension_table, how='left')
    data = data.drop('geography_fk', axis=1)
    data = data.rename({'instance': 'geography_fk'}, axis=1)
    
    dimension_table = {'federation_fk': pk_d_federation, 'instance': instance_d_federation}
    dimension_table = pd.DataFrame(dimension_table)
    data = pd.merge(data, dimension_table, how='left')
    data = data.drop('federation_fk', axis=1)
    data = data.rename({'instance': 'federation_fk'}, axis=1)
    
    dimension_table = {'age_group_fk': pk_d_age_group, 'instance': instance_d_age_group}
    dimension_table = pd.DataFrame(dimension_table)
    data = pd.merge(data, dimension_table, how='left')
    data = data.drop('age_group_fk', axis=1)
    data = data.rename({'instance': 'age_group_fk'}, axis=1)
    
    dimension_table = {'sexe_fk': pk_d_sexe, 'instance': instance_d_sexe}
    dimension_table = pd.DataFrame(dimension_table)
    data = pd.merge(data, dimension_table, how='left')
    data = data.drop('sexe_fk', axis=1)
    data = data.rename({'instance': 'sexe_fk'}, axis=1)
    
    dimension_table = {'date_fk': pk_d_date, 'instance': instance_d_date}
    dimension_table = pd.DataFrame(dimension_table)
    data = pd.merge(data, dimension_table, how='left')
    data = data.drop('date_fk', axis=1)
    data = data.rename({'instance': 'date_fk'}, axis=1)

    
    # Loading
    data = data.to_dict(orient='records')
    data = np.array(data)
    data = np.array_split(data, 10)
    data = [list(sublist) for sublist in data]
    for sublist in data:
        sublist = [F_Licence(**row) for row in sublist]
        F_Licence.objects.bulk_create(sublist)
            
