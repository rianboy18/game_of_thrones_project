# %load q03_eda_major_houses_on_attacking_side/build.py
import pandas as pd
import numpy as np
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.game_of_thrones.q01_feature_engineering.build import q01_feature_engineering
import matplotlib.pyplot as plt
plt.switch_backend('agg') 

battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')
battle, character_pred = q01_feature_engineering(battles,character_predictions)
df1 = battle
df2 = character_pred
def q03_eda_major_houses_on_attacking_side(battles):  
    battle['att_comm_count'].loc[battle['att_comm_count'].isnull()]=battle['att_comm_count'].loc[battle['att_comm_count'].isnull()].astype('object')
    battle['att_comm_count'] = battle['att_comm_count'].fillna(0)
    battles['att_comm_count'].value_counts().sort_index().plot.bar(rot =0)



