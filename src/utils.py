import pandas as pd
import os
import re


def get_title(name):
    title_search = re.search(' ([A-Za-z]+)\.', name)
    if title_search:
        return title_search.group(1)
    return ""


def get_data():
    print(__file__)
    file_name = os.path.dirname(__file__)
    file_loc = os.path.join(file_name, '..', 'data')
    raw_train = pd.read_csv(file_loc + '/train.csv')
    raw_test = pd.read_csv(file_loc + '/test.csv')
    df = pd.concat([raw_train, raw_test], axis=0)
    print(df.info())
    print(df.head())
    return df
