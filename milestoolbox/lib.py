# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for milestoolbox Project
"""
import numpy as np
import pandas as pd
import matplotlib
import requests
from bs4 import BeautifulSoup

def stocks(url):
    api_data = requests.get(url).json()
    apple_stock_df = pd.DataFrame(api_data)

    apple_stock_df['date'] = pd.to_datetime(apple_stock_df['date'], format="%Y-%m-%d")
    apple_stock_df = apple_stock_df.set_index('date')
    stock_history = apple_stock_df[['open', 'close', 'high', 'low']].plot(figsize=(12,4))

    return stock_history



# if __name__ == '__main__':
#     # For introspections purpose to quickly get this functions on ipython
#     import milestoolbox
#     folder_source, _ = split(milestoolbox.__file__)
#     df = pd.read_csv('{}/data/data.csv.gz'.format(folder_source))
#     clean_data = clean_data(df)
#     print(' dataframe cleaned')
