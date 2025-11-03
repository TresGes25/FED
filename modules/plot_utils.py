import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def make_charts(dataframe: pd.DataFrame) -> None:
    """
    This function reads in a pandas DataFrame.
    It produces a plot of annual GDP for each country.
    Nothing is returned.

    Args:
    dataframe: pd.DataFrame
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=dataframe, x='Year', y='GDP (millions USD)',
                 hue='Country', ax=ax)
    ax.set_xlabel('Year')
    ax.set_ylabel('GDP (million USD)')
    ax.set_title('GDP series')
    ax.legend
    plt.tight_layout()
    plt.show()
