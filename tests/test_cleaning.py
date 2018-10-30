from data_science_package.cleaning import to_float

import pandas as pd
import pandas.util.testing as tm
import pytest


def test_to_float_happy_path():
    int_col = [1, 2, 3]
    df = pd.DataFrame({"a": int_col, "b": [4, 5, 6]})
    float_col = [float(num) for num in int_col]
    expected_df = pd.DataFrame({"a": float_col, "b": [4, 5, 6]})

    result_df = to_float(df, "a")

    tm.assert_frame_equal(expected_df, result_df)


def test_to_float_bad_cols_param():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

    with pytest.raises(TypeError):
        result_df = to_float(df, None)
        return result_df


def test_exception_when_converting_string_to_float(makeMixedDataFrame):
    df = tm.makeMixedDataFrame()

    # convert string
    with pytest.raises(ValueError):
        to_float(df, "C")

    # convert datetime
    with pytest.raises(TypeError):
        to_float(df, "D")
