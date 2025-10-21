# %%
import pandas as pd

def read_data(path):

    df = pd.read_csv(path)

    df = df[["Reference area", "TIME_PERIOD", "OBS_VALUE"]]
    df.rename(columns={"Reference area" : "Country",
                    "TIME_PERIOD" : "Year",
                    "OBS_VALUE" : "GDP (millions USD)"}, inplace=True)

    print(df.head())

    return df
