"""_summary_
"""
    
import pandas as pd
import json
from app.models import ODS_Player
from rugby.settings import DATA_DIR, MAPPING_DIR

column_name_mapping = open(f"{MAPPING_DIR}/licence_mapping.json", 'rb').read()
column_name_mapping = json.loads(column_name_mapping)
 
def run():
    
    data = pd.read_csv(f"{DATA_DIR}/lic-data-2021.csv", sep=';', dtype=str)
    data = data.rename(column_name_mapping, axis=1)
    data = data.to_dict(orient='records')
    data = [ODS_Player(**row) for row in data]
    ODS_Player.objects.bulk_create(data)