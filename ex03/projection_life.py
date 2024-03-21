import datatable as dt
from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def convert_data(df: dt) -> dt:
    """convert data"""
    df = df.drop("country", axis=1)
    df = df.melt(var_name="year", value_name="pop")
    df["year"] = df["year"].astype(int)
    df["pop"] = df["pop"].str.replace("M", "").astype(float)
    return df


def projection_life(df: dt, df2: dt):
    """show graph"""
    try:
        columns_to_select = ['country', '1900']
        df = df[columns_to_select]
        df2 = df2[columns_to_select]
        merged_df = pd.merge(
            df,
            df2,
            on='country',
            suffixes=('_life_exp', '_gdp')
        )

        print(merged_df)

        plt.scatter(
            merged_df['1900_gdp'],
            merged_df['1900_life_exp']
        )
        plt.xscale("log")
        plt.xticks(
            [300, 1000, 10000],
            ["300", "1K", "10k"]
        )
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.savefig("life_expectancy_gdp.png")

    except Exception as e:
        print("error ", e)


if __name__ == "__main__":
    projection_life(
        load("life_expectancy_years.csv"),
        load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    )
