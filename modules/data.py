
import pandas as pd

def read_data(path):

    df = pd.read_csv(path)
    return df

def select_columns(df):
    df = df[["Reference area", "TIME_PERIOD", "OBS_VALUE"]]
    df = df.rename(columns={"Reference area" : "Country",
                    "TIME_PERIOD" : "Year",
                    "OBS_VALUE" : "GDP (millions USD)"})

    df["Year"] = pd.to_datetime(df["Year"], format="%Y")

    return df

def missing_data(df):

    num_missing = df.isnull().sum().sum()

    if num_missing > 0:
        df_clean = df.dropna()
        return df_clean
    else:
        return df

def load_data(path):

    df = read_data(path)
    df = select_columns(df)
    df = missing_data(df)

    return df
