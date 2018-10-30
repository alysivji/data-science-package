import pandas as pd
import pytest


@pytest.fixture
def getMixedTypeDict():
    index = pd.Index(['a', 'b', 'c', 'd', 'e'])

    data = {
        'A': [0., 1., 2., 3., 4.],
        'B': [0., 1., 0., 1., 0.],
        'C': ['foo1', 'foo2', 'foo3', 'foo4', 'foo5'],
        'D': pd.bdate_range('1/1/2009', periods=5)
    }

    return index, data


@pytest.fixture
def makeMixedDataFrame(getMixedTypeDict):
    return pd.DataFrame(getMixedTypeDict[1])
