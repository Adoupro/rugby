from app.models import Player
#import pandas as pd

def run():
    
    # Lire le fichier csv
    
    
    # Truncate de la table
    
    # Importer dans la table
    
    Player(first_name='Adou', last_name='DOUDOU')

    records = [Player(first_name='Adou', last_name='DOUDOU') for i in range(10000)]
    Player.objects.bulk_create(records)
    
    