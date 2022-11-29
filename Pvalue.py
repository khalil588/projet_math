import pandas as pd
import numpy as np
import scipy.stats as st

def create_pvalue_dataset(df,list_columns):
    lst_means = []
    for i in list_columns:
        d = {}
        d[i] = np.mean(df[i])
        lst_means.append(d)
    return lst_means

def create_data_set_p(df):
    list_columns = ['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']
    mean_values = create_pvalue_dataset(df, list_columns)
    print(mean_values)
    df_finale = pd.DataFrame()
    for i,column in enumerate(list_columns) :
        value = mean_values[i]
        df_finale[column]= df[column]- value[column]
    return df_finale







