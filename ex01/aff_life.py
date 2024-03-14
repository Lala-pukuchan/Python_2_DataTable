import pandas as pd
import datatable as dt
from load_csv import load

def aff_life(df: dt):
    """show graph"""
    try:
        france_df = df.loc[df['country'] == 'France']
        print(france_df)
        france_df = france_df.drop('country', axis=1)
        print(france_df)
        france_melted = france_df.melt(var_name='year', value_name='life_expectancy')
        print(france_melted)
    except:
        print("error ")

if __name__ == '__main__':
    aff_life(load('life_expectancy_years.csv'))