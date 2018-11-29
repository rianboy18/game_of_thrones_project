# %load q08_preprocessing/build.py
import pandas as pd
import numpy as np
import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from greyatomlib.game_of_thrones.q01_feature_engineering.build import q01_feature_engineering
from greyatomlib.game_of_thrones.q07_culture_survival.build import q07_culture_survival

battles = pd.read_csv('data/battles.csv')
character_predictions = pd.read_csv('data/character-predictions.csv')
death_preds=character_predictions


def q08_preprocessing(character_predictions):
    death_preds.loc[:, 'culture'] = [get_cult(x) for x in death_preds.culture.fillna('')]
    death_preds.loc[:, 'title'] = pd.factorize(death_preds.title)[0]
    death_preds.loc[:, 'culture'] = pd.factorize(death_preds.culture)[0]
    death_preds.loc[:, 'mother'] = pd.factorize(death_preds.mother)[0]
    death_preds.loc[:, 'father'] = pd.factorize(death_preds.father)[0]
    death_preds.loc[:, 'heir'] = pd.factorize(death_preds.heir)[0]
    death_preds.loc[:, 'house'] = pd.factorize(death_preds.house)[0]
    death_preds.loc[:, 'spouse'] = pd.factorize(death_preds.spouse)[0]

    death_preds.drop(['name', 'alive', 'pred', 'plod', 'isAlive', 'dateOfBirth'], 1, inplace = True)
    death_preds.columns = map(lambda x: x.replace('.', '').replace('_', ''), death_preds.columns)
    death_preds.fillna(value = -1, inplace = True)





