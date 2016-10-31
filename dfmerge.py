import pandas as pd
import os

os.chdir("/home/choiboy9106/Desktop/Metis/Project McNulty")

weatherdf = pd.read_csv("weather.csv")
sp500df = pd.read_csv("sp500.csv")
solardf = pd.read_csv("solar.csv")

df = pd.merge(weatherdf, solardf, on = "Date")
del df["Unnamed: 0"]
df = pd.merge(df, sp500df, on = "Date")
print(df)
del df["Unnamed: 0"]
df.to_csv("all.csv")


weatherdf = pd.read_csv("weather.csv")
vixdf = pd.read_csv("vix.csv")
solardf = pd.read_csv("solar.csv")

df = pd.merge(weatherdf, solardf, on = "Date")
del df["Unnamed: 0"]
df = pd.merge(df, vixdf, on = "Date")
print(df)
del df["Unnamed: 0"]
df.to_csv("all2.csv")
