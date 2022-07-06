'''
Assume df is a pandas dataframe object of the dataset given
'''

import numpy as np
import pandas as pd
import random


'''Calculate the entropy of the enitre dataset'''
# input:pandas_dataframe
# output:int/float
def get_entropy_of_dataset(df):
    entropy = 0
    tar = df[[df.columns[-1]]].values
    _, counts = np.unique(tar, return_counts=True)
    total_count = np.sum(counts)
    for i in counts:
        temp = i/total_count
        if temp != 0:
            entropy = entropy - temp*(np.log2(temp))
    return entropy


'''Return avg_info of the attribute provided as parameter'''
# input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
# output:int/float
def get_avg_info_of_attribute(df, attribute):
    
    at_val = df[attribute].values
    unique_at_val = np.unique(at_val)
    rows = df.shape[0]
    avg_info = 0
    for j in unique_at_val:
        df_slice = df[df[attribute] == j]
        tar = df_slice[[df_slice.columns[-1]]].values
        _, counts = np.unique(tar, return_counts=True)
        total_count = np.sum(counts)
        entropy = 0
        for i in counts:
            temp = i/total_count
            if temp != 0:
                entropy = entropy - temp*np.log2(temp)
        avg_info =avg_info + entropy*(np.sum(counts)/rows)
    return avg_info


'''Return Information Gain of the attribute provided as parameter'''
# input:pandas_dataframe,str
# output:int/float
def get_information_gain(df, attribute):
    information_gain = 0
    entr_attribute = get_avg_info_of_attribute(df, attribute)
    entr_dataset = get_entropy_of_dataset(df)
    information_gain = entr_dataset - entr_attribute  
    return information_gain



#input: pandas_dataframe
#output: ({dict},'str'
def get_selected_attribute(df):

    information_gains = {}
    selected_column = ''
    max_information_gain = float("-inf")
    for attribute in df.columns[:-1]:
        information_gain_of_attribute = get_information_gain(df, attribute)
        if information_gain_of_attribute > max_information_gain:
            selected_column = attribute
            max_information_gain = information_gain_of_attribute
        information_gains[attribute] = information_gain_of_attribute
    return (information_gains, selected_column)

    '''
    Return a tuple with the first element as a dictionary which has IG of all columns 
    and the second element as a string with the name of the column selected

    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
    '''
   
    pass
