#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import csv
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


#retrieve records from specified columns based on a given condition
def retrieve(data, condition_column, condition_value, column_names):
    
    #create an empty list to store the filtered records
    result = []

    #iterate through each item in the provided data
    for item in data:
        
        #check if the value of the specified condition_column in the current item matches the given condition_value
        if item[condition_column] == condition_value:
            
            #if the condition is met, create a new dictionary containing only the specified column_names and their corresponding values
            selected_columns = {column: item[column] for column in column_names}
            
            #append the selected_columns dictionary to the result list
            result.append(selected_columns)

    #display the result using the tabulate library with "fancy_grid" formatting
    print(tabulate(result, headers="keys", tablefmt="fancy_grid"))

