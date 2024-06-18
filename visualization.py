#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import csv
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import process as pr


# In[2]:


#determine proportions
def visualise_pie_chart(data, column, chart_title, legend_loc="lower right", bbox_to_anchor=(1.7, 0.0)):

    #group column of interest
    grouped_column = data.groupby(column)

    #determine size of each group
    group_size = grouped_column.size()

    #extract labels and counts
    group_list = group_size.index.tolist()
    group_count = group_size.tolist()
    
    #create figure
    plt.figure()

    #plot the pie chart using counts and labels
    plt.pie(group_count, labels=group_list)

    #create a title for the pie chart
    plt.title(chart_title)

    #add a legend to the pie chart, placing it using provided loc and bbox_to_anchor
    plt.legend(loc=legend_loc, bbox_to_anchor=bbox_to_anchor)

    #show the chart
    plt.show()


# In[3]:


#determine comparisons
def visualise_bar_chart(data, column, x_label, y_label, title, width=0.5):
    #group devices based on USB connector type
    data = data.groupby(column)

    #count the number of devices for each USB connector type
    group_size = data.size()

    #extract labels and counts
    group_list = group_size.index.tolist()
    group_count = group_size.tolist()

    #create figure
    plt.figure()

    #plot bar chart
    plt.bar(group_list, group_count, width=width)

    #create a label for x-axis and y-axis
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    #create a title for your graph
    plt.title(title)

    #show the graph
    plt.show()


# In[ ]:


def monthly_price_trend(data, start_year, end_year, x_label, y_label, title):
    
    currency = pr.get_user_input_dict("Enter currency. Please note that this program is case sensitive. : ", data, 'price_currency', str)
    
    #filter devices with prices in the specified currency
    devices_in_currency = data[data['price_currency'] == currency]

    #calculate the number of rows and columns for the subplots
    num_years = end_year - start_year + 1
    num_cols = 2
    num_rows = (num_years + 1) // 2 
    

    #create subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 5 * num_rows))
    fig.suptitle(title)

    #loop through the specified range of years
    for i, year in enumerate(range(start_year, end_year + 1)):
        #calculate the subplot position
        row = i // num_cols
        col = i % num_cols

        #filter by year
        devices_year = devices_in_currency[devices_in_currency['released_date'].dt.year == year]

        #group by month and calculate the mean price
        monthly_mean_prices = devices_year.groupby(devices_year['released_date'].dt.month)['price'].mean()

        #plot trend chart on the corresponding subplot
        axes[row, col].plot(monthly_mean_prices.index, monthly_mean_prices.values, marker='o')
        axes[row, col].set_title(str(year))
        axes[row, col].set_xlabel(x_label)
        axes[row, col].set_ylabel(y_label)

    #adjust layout and show the plot
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust the subplot layout
    plt.show()


# In[8]:


#visualize scatter plot with a trend line

def scatter_plot(data, column1, column2, x_label, y_label, chart_title): 

    #extract display_diagonal column from original data frame
    feature1 = data[column1]

    #extract pixel_density column from original data frame
    feature2 = data[column2]
    
    #create a figure
    plt.figure(figsize=(12,8))
    
    #plot a scatter chart
    plt.scatter(feature1, feature2)

    #create a label for x-axis, y-axis and chart title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(chart_title)

    #show the graph
    plt.show()

