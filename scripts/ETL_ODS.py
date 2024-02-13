"""_summary_
"""
    
import pandas as pd
<<<<<<< HEAD
import json
from app.models import ODS_Player
from rugby.settings import DATA_DIR, MAPPING_DIR

column_name_mapping = open(f"{MAPPING_DIR}/licence_mapping.json", 'rb').read()
column_name_mapping = json.loads(column_name_mapping)
=======
from app.models import ODS_Player
from rugby.settings import DATA_DIR

column_name_mapping = {
    'Code Commune': 'code_commune',
    'Commune': 'commune',
    'Code QPV': 'code_qpv',
    'Nom QPV': 'nom_qpv',
    'Département': 'departement',
    'Région': 'region',
    'Statut géo': 'statut_geo',
    'Code': 'code',
    'Fédération': 'federation',
    'F - 1 à 4 ans': 'f_1_4_ans',
    'F - 5 à 9 ans': 'f_5_9_ans',
    'F - 10 à 14 ans': 'f_10_14_ans',
    'F - 15 à 19 ans': 'f_15_19_ans',
    'F - 20 à 24 ans': 'f_20_24_ans',
    'F - 25 à 29 ans': 'f_25_29_ans',
    'F - 30 à 34 ans': 'f_30_34_ans',
    'F - 35 à 39 ans': 'f_35_39_ans',
    'F - 40 à 44 ans': 'f_40_44_ans',
    'F - 45 à 49 ans': 'f_45_49_ans',
    'F - 50 à 54 ans': 'f_50_54_ans',
    'F - 55 à 59 ans': 'f_55_59_ans',
    'F - 60 à 64 ans': 'f_60_64_ans',
    'F - 65 à 69 ans': 'f_65_69_ans',
    'F - 70 à 74 ans': 'f_70_74_ans',
    'F - 75 à 79 ans': 'f_75_79_ans',
    'F - 80 à 99 ans': 'f_80_99_ans',
    'F - NR': 'f_nr',
    'H - 1 à 4 ans': 'h_1_4_ans',
    'H - 5 à 9 ans': 'h_5_9_ans',
    'H - 10 à 14 ans': 'h_10_14_ans',
    'H - 15 à 19 ans': 'h_15_19_ans',
    'H - 20 à 24 ans': 'h_20_24_ans',
    'H - 25 à 29 ans': 'h_25_29_ans',
    'H - 30 à 34 ans': 'h_30_34_ans',
    'H - 35 à 39 ans': 'h_35_39_ans',
    'H - 40 à 44 ans': 'h_40_44_ans',
    'H - 45 à 49 ans': 'h_45_49_ans',
    'H - 50 à 54 ans': 'h_50_54_ans',
    'H - 55 à 59 ans': 'h_55_59_ans',
    'H - 60 à 64 ans': 'h_60_64_ans',
    'H - 65 à 69 ans': 'h_65_69_ans',
    'H - 70 à 74 ans': 'h_70_74_ans',
    'H - 75 à 79 ans': 'h_75_79_ans',
    'H - 80 à 99 ans': 'h_80_99_ans',
    'H - NR': 'h_nr',
    'NR - NR': 'nr_nr',
    'Total': 'total',
}

>>>>>>> 8587be5b023a907496125a2d01ba360ffda11eb6
 
def run():
    
    data = pd.read_csv(f"{DATA_DIR}/lic-data-2021.csv", sep=';', dtype=str)
    data = data.rename(column_name_mapping, axis=1)
    data = data.to_dict(orient='records')
    data = [ODS_Player(**row) for row in data]
    ODS_Player.objects.bulk_create(data)