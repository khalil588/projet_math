import random
import time
import warnings
from Pvalue import create_data_set_p
warnings.simplefilter(action='ignore', category=FutureWarning)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import  scipy.stats as st
# this function help us recreate a new data set that is based on the old dataset
def recreate_dataset(df):

    df2 = pd.DataFrame()
    for i in range(10752):
        r = random.randint(0, 10751)
        df2 = df2.append(df.loc[r])
    return df2

# the purpose from this function is to create a dataset based on the means of the bootstrapped datasets
def create_mean_data_set(df) :
    df_mean = pd.DataFrame()
    for i in range(40):
        df_mean= df_mean.append(recreate_dataset(df).mean(),ignore_index=True)
        print('done number '+str(i))
    return df_mean
# this function's goal is to show the histograms based on the means data set
def show_hist(df,lst):
    df_mean = create_mean_data_set(df)
    df_test_pvalue = create_mean_data_set(create_data_set_p(df))

    for i in lst :
        plt.hist(df_mean[i],bins=8)
        plt.title('Bootstraping mean result !!')
        plt.xlabel('means of '+i )
        plt.ylabel('values !!!')
        i_confiance = st.norm.interval(alpha=0.95,
                 loc=np.mean(df_mean[i]),
                 scale=st.sem(df_mean[i]))
        print("Les valeurs de l'intervalle de confiance , erreur standard , test d'hypothese du colonne "+i)
        print("L'intervalle de confiance est égale à [ "+ str(i_confiance[0])+" , "+str(i_confiance[1])+" ]")
        print("l'erreur standard est égale à " + str(st.sem(df_mean[i])))
        print("la valeur du p du colonne "+i+ " :  ")
        print( st.ttest_ind(df_mean[i],df_test_pvalue[i]))

        plt.show()
df = pd.read_csv('ADP_DATA1.csv')
list_columns = ['High','Low','Open','Close','Volume','Adj Close']
show_hist(df,list_columns)
print('DONE !!')
# test d'hypthese / standard errors
""" 
(44.4233435113263, 44.63495910011613)
(44.75015635460438, 44.964711208330975)
(44.87237441269891, 45.08663795735709)
(2057931.0277771591, 2064343.9565606387)
(37.3819850551305, 37.588207854616215)
"""