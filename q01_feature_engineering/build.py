# %load q01_feature_engineering/build.py
import pandas as pd
import numpy as np

battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')
df2 = character_predictions
def q01_feature_engineering(battles,character_predictions):
    
    battles['attacker_commander'] = battles['attacker_commander'].fillna(battles['attacker_commander'].mode()[0])
    battles['defender_1'] = battles['defender_1'].fillna(battles['defender_1'].mode()[0])
    battles['defender_2'] = battles['defender_2'].fillna(battles['defender_2'].mode()[0])
    battles['defender_3'] = battles['defender_3'].fillna(0)
    battles['defender_4'] = battles['defender_4'].fillna(0)
    battles['defender_count'] = 2
    battles['attacker_count'] = 4
    battles['att_comm_count'] = battles['attacker_commander'].str.split(',').str.len()
    df2['no_of_books'] = df2['book1']+df2['book2']+df2['book3']+df2['book4']+df2['book5']
    return battles,df2





