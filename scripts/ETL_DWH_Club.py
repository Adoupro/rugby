"""_summary_
"""

import pandas as pd
import json
from django.db.models import Q
from app.models import ODS_Club, D_Geography
from rugby.settings import DATA_DIR, MAPPING_DIR

d_geography_mapping = open(f"{MAPPING_DIR}/club_geography_mapping.json", 'rb').read()
d_geography_mapping = json.loads(d_geography_mapping)

queryset = ODS_Club.objects.filter(~Q(code_commune="NR - Non réparti"))

def run():
    
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
    data = data.to_dict(orient='records')
    data = [D_Geography(**row) for row in data]
    D_Geography.objects.bulk_create(data)