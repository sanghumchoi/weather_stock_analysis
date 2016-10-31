import pandas as pd

weatherdf = pd.read_csv("nyc_data.csv")
weatherdf = weatherdf.rename(columns = lambda x: x.strip())
weatherdf["Date"] = pd.to_datetime(weatherdf[["Year", "Month", "Day"]])

del weatherdf["Day"]
del weatherdf["JD"]
del weatherdf["JD_prcp"]
del weatherdf["Month"]
del weatherdf["State_id"]
del weatherdf["Year"]
del weatherdf["JD_snow"]
del weatherdf["CPRC (in)"]
del weatherdf["CPRS (in)"]
del weatherdf["PRCP_flag"]
del weatherdf["SNOW_flag"]
del weatherdf["SNWD_flag"]
del weatherdf["CSNW (in)"]
del weatherdf["Season_prcp"]
del weatherdf["Season_snow"]
del weatherdf["TMIN_flag"]
del weatherdf["TMAX_flag"]
weatherdf.columns = ["Precipitation", "Snowfall", "Snow Depth", "Average Temperature", "Max Temperature", "Min Temperature", "Date"]

weatherdf.to_csv("weather.csv")
