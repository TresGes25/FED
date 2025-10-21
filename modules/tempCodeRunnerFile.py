df = pd.read_csv("./Data.csv")
print(df.columns)

df = df[["Reference area", "TIME_PERIOD", "OBS_VALUE"]]
df.rename(columns={"Reference area" : "Country",
                   "TIME_PERIOD" : "Year",
                   "OBS_VALUE" : "Value (millions USD)"}, inplace=True)

print(df.head())