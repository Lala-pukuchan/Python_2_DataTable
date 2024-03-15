import datatable as dt
from load_csv import load
import matplotlib.pyplot as plt


def aff_life(df: dt):
    """show graph"""
    try:
        france_df = df.loc[df["country"] == "France"]
        france_df = france_df.drop("country", axis=1)
        france_melted = france_df.melt(var_name="year", value_name="ex")
        france_melted["year"] = france_melted["year"].astype(int)
        plt.plot(france_melted["year"], france_melted["ex"])
        plt.xticks(
            range(france_melted["year"].min(), france_melted["year"].max() + 1, 40)
        )
        plt.title("France Life expectancy Projections")
        plt.xlabel("year")
        plt.ylabel("life expectancy")
        plt.savefig("life_expectancy_years.png")
    except Exception as e:
        print("error ", e)


if __name__ == "__main__":
    aff_life(load("life_expectancy_years.csv"))
