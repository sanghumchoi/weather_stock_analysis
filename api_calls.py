import requests
import pandas as pd
import io
import os

os.chdir("/home/choiboy9106/Desktop/Metis/Project McNulty")

# SP500 API Call
url = "https://www.quandl.com/api/v3/datasets/YAHOO/INDEX_GSPC.csv?api_key=dpxn7UxEEZjQENpNyNML&start_date=2003-12-31"
response = requests.get(url).content
sp500df = pd.read_csv(io.StringIO(response.decode('utf-8')))
sp500df["HiLoRange"] = sp500df["High"] - sp500df["Low"]
sp500df["OpClRange"] = sp500df["Open"] - sp500df["Close"]
sp500df["Direction"] = ""
for i in range(len(sp500df)):
    if sp500df["OpClRange"][i] > 0:
        sp500df["Direction"][i] = "Up"
    if sp500df["OpClRange"][i] < 0:
        sp500df["Direction"][i] = "Down"
sp500df["Date"] = pd.to_datetime(sp500df["Date"])
sp500df.to_csv("sp500.csv")

# VIX API Call
url1 = "https://www.quandl.com/api/v3/datasets/YAHOO/INDEX_VIX.csv?api_key=dpxn7UxEEZjQENpNyNML&start_date=2004-01-01"
response1 = requests.get(url1).content
vixdf = pd.read_csv(io.StringIO(response1.decode('utf-8')))
vixdf["HiLoRange"] = vixdf["High"] - vixdf["Low"]
vixdf["OpClRange"] = vixdf["Open"] - vixdf["Close"]
vixdf["Direction"] = ""
for i in range(len(vixdf)):
    if vixdf["OpClRange"][i] > 0:
        vixdf["Direction"][i] = "Up"
    if vixdf["OpClRange"][i] < 0:
        vixdf["Direction"][i] = "Down"
vixdf["Date"] = pd.to_datetime(vixdf["Date"])
vixdf.to_csv("vix.csv")
