#Create Monthly Values

import pandas as pd
from zipfile import ZipFile
import os

def prepare():
    SCRIPTDIR = os.path.dirname(__file__).rstrip("\code")
    ZIPDIR=SCRIPTDIR + "\data\weather.zip"
    OUTPUTDIR=SCRIPTDIR + "\data"
    YAMLFILE = os.path.join(SCRIPTDIR, 'params\\fileParams.yml')
    with ZipFile(ZIPDIR, 'r') as zObject: 
        zObject.extractall(path=OUTPUTDIR)
        
    files = os.listdir(OUTPUTDIR)
    files = [file for file in files if file.endswith('.csv')]

    file_name = ''
    
    for f in files:
        data = pd.read_csv(os.path.join(OUTPUTDIR, f))
        if data['MonthlyDepartureFromNormalAverageTemperature'].isnull().sum() < len(data['MonthlyDepartureFromNormalAverageTemperature']) and data['DailyDepartureFromNormalAverageTemperature'].isnull().sum() < len(data['DailyDepartureFromNormalAverageTemperature']):
            file_name = f 
            field_name = 'DailyDepartureFromNormalAverageTemperature'
            with open(YAMLFILE, 'w') as file:
                file.write(f'file_name: {file_name}\n')
                file.write(f'field_name: {field_name}\n')
    
    monthlyValues = data['MonthlyDepartureFromNormalAverageTemperature']
    monthlyValues.dropna(inplace=True)

    monthlyValues.to_csv(SCRIPTDIR+'/output/monthlyValues.csv', index=False)

prepare()