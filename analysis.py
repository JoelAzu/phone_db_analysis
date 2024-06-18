#!/usr/bin/env python
# coding: utf-8

# In[31]:


import os
import csv
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import process as pr


# In[32]:


#calculate top 5 sales region for particular brand
def top5_sales_region(data):
    
    specific_brand = pr.get_user_input_dict('Enter the brand. : ', data, 'brand', str)
    
    #grouping by brand
    brand_grouped = data.groupby('brand')

    #selcting specific brand
    specific_brand = brand_grouped.get_group(specific_brand)
    
    #splitting column
    specific_brand_split = specific_brand['market_regions'].str.split(',')
    
    #exploding column
    specific_brand_explode = specific_brand_split.explode()
    
    #counting values
    top_5 = specific_brand_explode.value_counts()

    #saving into a new df for better presentation
    top_5_df = pd.DataFrame({'count': top_5})

    #displaying df
    return top_5_df.head().reset_index()


# In[33]:


#calculate mean price for particular brand and currency
def brand_mean_price(data):
    
    #get target value input
    value1 = pr.get_user_input_dict("Enter brand. Please note that this program is case sensitive. : ", data, 'brand', str, error_message="Invalid input. Please try again.")
    value2 = pr.get_user_input_dict("Enter currency. Please note that this program is case sensitive. : ", data, 'price_currency', str, error_message="Invalid input. Please try again.")
    
    #filter for specified brand and currency
    price_df = data.loc[(data['brand'] == value1) & (data['price_currency'] == value2), :]

    #calculate the average price of specified brand in specified currency
    currency_mean = price_df['price'].mean()

    #print the average price of specified brand in specified currency
    print(f"\n{value1} mean price sales in {value2} is: {currency_mean:.2f}.\n")


# In[34]:


#calculate average mass
def mean_mass(data, column):
    
    #group by specified column and calculate average weight for that category
    avg_mass = data.groupby(column)['weight_gram'].mean().round(2)

    #save result into a new data frame
    avg_mass_df = pd.DataFrame({'Mass': avg_mass})

    #reset the index of the data frame
    avg_mass_reset = avg_mass_df.reset_index()

    #display the data frame with reset index   
    return avg_mass_reset


# In[36]:


#calculate least expensive gadgets in chosen currency
def cheapest_devices(data):
    
    #get target currency input
    currency = pr.get_user_input_dict("Enter currency. Please note that this program is case sensitive. : ", data, 'price_currency', str)
    
    #filter for devices in chosen currency
    device_in_currency = data.loc[data['price_currency'] == currency]

    #sort in ascending order to display the 5 least expensive devices in chosen currency
    lowest_5 = device_in_currency.sort_values(by = ['price'], inplace =False, ascending=True)
    
    #select fundamental info for better presentation
    lowest_5_select = lowest_5[['brand','codename', 'price']]
    
    #display the 5 least expensive devices in chosen currency
    return lowest_5_select.reset_index(drop=True).head(5)

