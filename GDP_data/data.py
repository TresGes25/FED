import pandas as pd


# add type hints AND docstrings
def read_data(path: str) -> pd.DataFrame:
    """
    This function reads in a csv file (a string indicating the path is passed).
    It returns a pandas DataFrame.

    Args:
    path: str
    """
    df = pd.read_csv(path)
    return df


def select_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function reads in a pandas DataFrame.
    It returns a pandas DataFrame with select renamed columns.

    Args:
    df: pd.DataFrame
    """
    df = df[["Reference area", "TIME_PERIOD", "OBS_VALUE"]]
    df = df.rename(columns={"Reference area": "Country",
                            "TIME_PERIOD": "Year",
                            "OBS_VALUE": "GDP (millions USD)"})

    df["Year"] = pd.to_datetime(df["Year"], format="%Y")

    return df


def missing_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function reads in a pandas DataFrame and inspects it.
    It returns a pandas DataFrame with no missing observations.

    Args:
    df: pd.DataFrame
    """
    num_missing = df.isnull().sum().sum()

    if num_missing > 0:
        df_clean = df.dropna()
        return df_clean
    else:
        return df


def load_data(path: str) -> pd.DataFrame:
    """
    This function takes in a str path and uses it to load a pandas DataFrame.
    The df undergoes column selection and missing data handling.
    The dataframe is then returned.

    Args:
    path: str
    """
    df = read_data(path)
    df = select_columns(df)
    df = missing_data(df)

    return df
