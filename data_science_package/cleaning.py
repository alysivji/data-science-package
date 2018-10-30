from collections.abc import Iterable
from typing import List, Union

import pandas as pd


def to_float(df: pd.DataFrame, cols: Union[str, List[str]]) -> pd.DataFrame:
    """Give a dataframe, returns a new dataframe"""
    cols_to_convert = []
    if isinstance(cols, str):
        cols_to_convert = {cols: "float"}
    elif isinstance(cols, Iterable):
        cols_to_convert = {col: "float" for col in cols}
    else:
        raise TypeError("col needs to be string or iterable")

    df_copy = df.copy(deep=True)
    return df_copy.astype(cols_to_convert)
