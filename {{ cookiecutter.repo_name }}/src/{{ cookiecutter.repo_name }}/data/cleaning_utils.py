import pandas as pd
from typing import Union


def replace_value_by_mean(
    df: pd.DataFrame, column: str, value: Union[int, float]
) -> None:
    temp = df[df[column] != value]
    mean = temp[column].mean()

    indices = df[df[column] == value].index
    df.loc[indices, column] = mean
