"""_summary_
"""
    
import pandas as pd
import json
from app.models import ODS_Club
from rugby.settings import DATA_DIR, MAPPING_DIR

column_name_mapping = open(f"{MAPPING_DIR}/club_mapping.json", 'rb').read()
column_name_mapping = json.loads(column_name_mapping)
 
def run():
    
    file_name = f"clubs-data-2021.csv"
    data = pd.read_csv(f"{DATA_DIR}/{file_name}", sep=';', dtype=str)
    data['file_name'] = file_name
    data = data.rename(column_name_mapping, axis=1)
    data = data.to_dict(orient='records')
    data = [ODS_Club(**row) for row in data]
    ODS_Club.objects.bulk_create(data)