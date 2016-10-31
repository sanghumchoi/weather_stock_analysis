import pandas as pd
import os

os.chdir("/home/choiboy9106/Desktop/Metis/Project McNulty")

df1 = pd.read_csv("1232037_40.77_-73.98_2004.csv")
df2 = pd.read_csv("1232037_40.77_-73.98_2005.csv")
df3 = pd.read_csv("1232037_40.77_-73.98_2006.csv")
df4 = pd.read_csv("1232037_40.77_-73.98_2007.csv")
df5 = pd.read_csv("1232037_40.77_-73.98_2008.csv")
df6 = pd.read_csv("1232037_40.77_-73.98_2009.csv")
df7 = pd.read_csv("1232037_40.77_-73.98_2010.csv")
df8 = pd.read_csv("1232037_40.77_-73.98_2011.csv")
df9 = pd.read_csv("1232037_40.77_-73.98_2012.csv")
df10 = pd.read_csv("1232037_40.77_-73.98_2013.csv")
df11 = pd.read_csv("1232037_40.77_-73.98_2014.csv")
df12 = pd.read_csv("1232037_40.77_-73.98_2015.csv")

def csvcleaning(df):
    del df["DHI"]
    del df["DNI"]
    del df["GHI"]
    del df["Cloud Type"]
    del df["Temperature"]
    del df["Fill Flag"]
    df["Date"] = pd.to_datetime(df[["Year", "Month", "Day"]])
    del df["Year"]
    del df["Month"]
    del df["Day"]
    del df["Hour"]
    del df["Minute"]
    df = pd.pivot_table(df, index = "Date", aggfunc = "mean")
    return df

df1 = csvcleaning(df1)
df2 = csvcleaning(df2)
df3 = csvcleaning(df3)
df4 = csvcleaning(df4)
df5 = csvcleaning(df5)
df6 = csvcleaning(df6)
df7 = csvcleaning(df7)
df8 = csvcleaning(df8)
df9 = csvcleaning(df9)
df10 = csvcleaning(df10)
df11 = csvcleaning(df11)
df12 = csvcleaning(df12)

solardf = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12])
solardf.to_csv("solar.csv")
