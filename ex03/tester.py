from projection_life import projection_life
from load_csv import load

projection_life(
    load("life_expectancy_years.csv"), 
    load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
)
