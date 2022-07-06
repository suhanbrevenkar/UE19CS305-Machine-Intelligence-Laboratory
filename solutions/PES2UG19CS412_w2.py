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
    # TODO
    unique_value = df['play'].value_counts()
    total_value = df['play'].shape[0]
    a = len(unique_value)
    entropy = 0
    for o in range(a):
    	t = unique_value[o]/total_value
    	if t != 1:
    		entropy += -1*(t)*np.emath.logn(a,t)
    return entropy


'''Return average_info of the attribute provided as parameter'''
# input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
# output:int/float
def get_avg_info_of_attribute(df, attribute):
    # TODO
    attribute_value = df[attribute].value_counts().to_dict()
    total_attribute_n = df[attribute].shape[0]
    average_info = 0
    for att in attribute_value:
    	att_df = df[df[attribute] == att]
    	average_info += (attribute_value[att]/total_attribute_n)*get_entropy_of_dataset(att_df)
    return average_info


'''Return Information Gain of the attribute provided as parameter'''
# input:pandas_dataframe,str
# output:int/float
def get_information_gain(df, attribute):
    # TODO
    entropy_df = get_entropy_of_dataset(df)
    information_gain = entropy_df - get_avg_info_of_attribute(df, attribute)
    return information_gain




#input: pandas_dataframe
#output: ({dict},'str')
def get_selected_attribute(df):
    '''
    Return a tuple with the first element as a dictionary which has IG of all columns 
    and the second element as a string with the name of the column selected
    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
    '''
    # TODO
    column_list = df.columns.to_list()
    column_list.remove('play')
    dict_ig = {}
    for column in column_list:
    	dict_ig[column] = get_information_gain(df, column)
    return (dict_ig, max(dict_ig, key=lambda x: dict_ig[x]))
