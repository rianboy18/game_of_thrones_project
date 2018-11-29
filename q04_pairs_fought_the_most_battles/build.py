# %load q04_pairs_fought_the_most_battles/build.py
import pandas as pd
from collections import Counter
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
def q04_pairs_fought_the_most_battles(battles):
    c = list(Counter([tuple(set(x)) for x in battles.dropna(subset = ['attacker_king', 'defender_king'])[['attacker_king', 'defender_king']].values if len(set(x)) > 1]).items())
    pd.DataFrame(c).sort_values(1).plot.barh(figsize = (10, 6))
    pd.DataFrame(c).sort_values(1).plot.barh(figsize = (10, 6)).set(yticklabels = ['%s vs. %s' % (x[0], x[1]) for x in list(zip(*c))[0]], xlabel = 'No. of Battles'), pd.DataFrame(c).sort_values(1).plot.barh(figsize = (10, 6)).legend('')
    return c
    
    
    
    


