from data_science_package.cleaning import to_float

import pandas as pd
import pandas.util.testing as tm
import pytest


def test_to_float_happy_path():
    # Arrange
    int_col = [1, 2, 3]
    df = pd.DataFrame({"a": int_col, "b": [4, 5, 6]})
    float_col = [float(num) for num in int_col]
    expected_df = pd.DataFrame({"a": float_col, "b": [4, 5, 6]})

    # Act
    result_df = to_float(df, "a")

    # Assert
    tm.assert_frame_equal(expected_df, result_df)


def test_to_float_bad_cols_param():
    # Arrange
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

    # Act / Assert
    with pytest.raises(TypeError):
        result_df = to_float(df, None)
        return result_df


def test_exception_when_converting_string_to_float(makeMixedDataFrame):
    # Arrange
    df = makeMixedDataFrame

    # Act / Assert (string)
    with pytest.raises(ValueError):
        to_float(df, "C")

    # Act / Assert (datetime)
    with pytest.raises(TypeError):
        to_float(df, "D")
