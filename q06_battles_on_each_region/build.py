# %load q06_battles_on_each_region/build.py
import pandas as pd
import numpy as np
import seaborn as sns
sns.set_style('white')
import matplotlib.pyplot as plt
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.game_of_thrones.q01_feature_engineering.build import q01_feature_engineering
plt.switch_backend('agg') 

battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')

df2 = character_predictions
battles['attacker_commander'] = battles['attacker_commander'].fillna(battles['attacker_commander'].mode()[0])
battles['defender_1'] = battles['defender_1'].fillna(battles['defender_1'].mode()[0])
battles['defender_2'] = battles['defender_2'].fillna(battles['defender_2'].mode()[0])
battles['defender_3'] = battles['defender_3'].fillna(0)
battles['defender_4'] = battles['defender_4'].fillna(0)
battles['defender_count'] = 2
battles['attacker_count'] = 4
battles['att_comm_count'] = battles['attacker_commander'].str.split(',').str.len()
df2['no_of_books'] = df2['book1']+df2['book2']+df2['book3']+df2['book4']+df2['book5']

def q06_battles_on_each_region(df2):
    data = battles.groupby('region').sum()[['major_death', 'major_capture']]
    p=pd.concat([data, battles.region.value_counts().to_frame()], axis = 1).sort_values('region', ascending = False).copy(deep = True).plot.bar(color = [sns.color_palette()[1], 'grey', 'darkblue'], rot = 0)
    p.set(xlabel = 'Region', ylabel = 'No. of Events') 
    p.legend(['Major Deaths', 'Major Captures', 'No. of Battles'], fontsize = 16)
    plt.show()
    return data
c =  q06_battles_on_each_region(df2)
c


