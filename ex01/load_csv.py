import pandas as pd
import datatable as dt

def load(path: str) -> dt:
    """load csv"""
    try:
        pd_df = pd.read_csv(path)
        print("Loading dataset of dimensions ", pd_df.shape)
        return pd_df
    except:
        return None

if __name__ == '__main__':
    load('life_expectancy_years.csv')