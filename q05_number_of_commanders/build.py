# %load q05_number_of_commanders/build.py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
sns.set_style('white')
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


battles.head()
def q05_number_of_commanders(battles):
    sns.boxplot('att_comm_count', 'attacker_king', data = battles, saturation = .6, fliersize = 10., palette = ['lightgray', sns.color_palette()[1], 'grey', 'darkblue'])
    sns.boxplot('att_comm_count', 'attacker_king', data = battles, saturation = .6, fliersize = 10., palette = ['lightgray', sns.color_palette()[1], 'grey', 'darkblue']).set(xlabel = 'No. of Attacker Commanders', ylabel = 'Attacker King', xticks = range(8))


c =  q05_number_of_commanders(battles)


