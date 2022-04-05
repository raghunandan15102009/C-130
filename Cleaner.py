import pandas as pd
import csv
df = pd.read_csv('merged_data.csv')
del df['luminosity']
del df['lum']
df = df.rename({
                'Radius' : 'Solar_Radius',
                'Mass' : 'Solar_Mass'
                },axis = 'columns')
df.to_csv('main.csv')