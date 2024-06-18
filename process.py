#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#get file path from user
def get_file_path():
    while True:
        try:
            path_input = str(input("Enter a file path: "))
            if os.path.exists(path_input):
                print(f"You have successfully entered a file path.")
                return path_input
            else:
                print(f"File not found at: {path_input}. Please try again.")
        except (TypeError, FileNotFoundError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}. Please try again.")


# In[3]:


#load data based on user specification of file path
def load_data_csv(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
            print("The specified file has been loaded successfully.")
        return data
    except (IOError, FileNotFoundError):
        print(f"Error: File not found at {file_path}")


# In[4]:


#load data with pandas
def load_data_pandas(file_path):
    try:
        data = pd.read_csv(file_path, encoding='utf-8')
        print("The specified file has been loaded successfully.")
        return data
    except (IOError, FileNotFoundError):
        print("File does not exist. Try again!") 


# In[7]:


#validate that input matches values in specific list column 
def get_user_input_list(prompt, data, condition_column, data_type, error_message="Invalid input. Please try again."):
    while True:
        try:
            user_input = data_type(input(prompt))
            if user_input in [row[condition_column] for row in data]:
                return user_input
            else:
                print(error_message)
        except ValueError:
            print(error_message)


# In[8]:


#validate that input matches values in specific dictionary column 
def get_user_input_dict(prompt, data, condition_column, data_type, error_message="Invalid input. Please try again."):
    while True:
        try:
            user_input = data_type(input(prompt))
            if user_input in data[condition_column].values:
                return user_input
            else:
                print(error_message)
        except (KeyError, ValueError):
            print(error_message)

