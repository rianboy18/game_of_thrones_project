# %load q02_eda_major_death/build.py
import pandas as pd
import numpy as np
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.game_of_thrones.q01_feature_engineering.build import q01_feature_engineering
import matplotlib.pyplot as plt

battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')
battles, character_pred = q01_feature_engineering(battles,character_predictions)
df1 = battles
df2 = character_predictions

def q02_eda_major_death(battles):
    df3=df1.groupby(['year'])['major_death','major_capture'].sum()
    df3.plot(x='year', y=['major_death','major_capture'], kind='bar')




