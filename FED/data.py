#Script to load and clean the data
import pandas as pd

def load_data(data):
    """A function that loads in a CSV file
    input is a path that leads to a CSV file"""

    return pd.read_csv(data)


#%%
df = load_data("Data.csv")
df.head()
#%%