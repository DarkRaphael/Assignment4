#Evaluate R2 Score
from sklearn.metrics import r2_score
import pandas as pd
import os

def evaluate():
    SCRIPTDIR = os.path.dirname(__file__).rstrip("\code")
    OUTPUTDIR=SCRIPTDIR + "\data"
    YAMLFILE = os.path.join(SCRIPTDIR, 'params\\fileParams.yml')

    monthlyValues = pd.read_csv(SCRIPTDIR+'/output/monthlyValues.csv')
    monthlyValuesComputed = pd.read_csv(SCRIPTDIR+'/output/monthlyComputed.csv')
    if len(monthlyValues) != len(monthlyValuesComputed):
        if len(monthlyValues) > len(monthlyValuesComputed):
            monthlyValues = monthlyValues[:len(monthlyValuesComputed)]
        else:
            monthlyValuesComputed = monthlyValuesComputed[:len(monthlyValues)]
    r2 = r2_score(monthlyValues, monthlyValuesComputed)
    if r2 >= 0.9:
        print('The dataset is consistent')
    else:
        print('The dataset is not consistent')
    return r2

evaluate()