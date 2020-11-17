# -*- coding: UTF-8 -*-

# Import from standard library
import os
import milestoolbox
import pandas as pd
# Import from our lib
import pytest
from milestoolbox.lib import stocks

def test_stocks():
    url = 'http://iex.lewagon.com/stable/stock/aapl/chart/3m'
    apple = stocks(url)
    assert isinstance(apple, pd.DataFrame)

# def test_clean_data():
#     datapath = os.path.dirname(os.path.abspath(milestoolbox.__file__)) + '/data'
#     df = pd.read_csv('{}/data.csv.gz'.format(datapath))
#     first_cols = ['id', 'civility', 'birthdate', 'city', 'postal_code', 'vote_1']
#     assert list(df.columns)[:6] == first_cols
#     assert df.shape == (999, 142)
#     out = clean_data(df)
#     assert out.shape == (985, 119)
