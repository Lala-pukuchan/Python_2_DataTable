import datatable as dt
from load_csv import load
import matplotlib.pyplot as plt


def convert_data(df: dt) -> dt:
    """convert data"""
    df = df.drop("country", axis=1)
    df = df.melt(var_name="year", value_name="pop")
    df["year"] = df["year"].astype(int)
    df["pop"] = df["pop"].str.replace("M", "").astype(float)
    return df


def aff_pop(df: dt):
    """show graph"""
    try:
        france_df = df.loc[df["country"] == "France"]
        print(france_df)
        france_melted = convert_data(france_df)
        print(france_melted)

        belgium = df.loc[df["country"] == "Belgium"]
        print(belgium)
        belgium_melted = convert_data(belgium)
        print(belgium_melted)

        plt.plot(
            france_melted["year"],
            france_melted["pop"],
            label="France"
        )
        plt.plot(
                belgium_melted["year"],
                belgium_melted["pop"],
                label="Belgium"
            )
        plt.legend()
        plt.xticks(
            range(
                france_melted["year"].min(),
                france_melted["year"].max() + 1,
                40
            )
        )
        plt.yticks(
            range(0, 70, 20),
            [f'{y}M' for y in range(0, 70, 20)]
        )
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.savefig("populdation_total.png")
    except Exception as e:
        print("error ", e)


if __name__ == "__main__":
    aff_pop(load("populdation_total.csv"))
