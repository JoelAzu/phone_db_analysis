#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import csv
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


LINE_WIDTH = 85

def started(msg=""):
    output = f"Program started: {msg}..."
    dashes = "-" * LINE_WIDTH
    print(f"{dashes}\n{output}\n")


# In[4]:


def completed():
    dashes = "-" * LINE_WIDTH
    print(f"\nOperation completed.\n{dashes}\n")


# In[15]:


def menu():
    
    while True:
        
        print("\nChoose an option from the menu list:\n")

        print("RETRIEVAL:")
        print("1. Retrieval Based on OEM ID")
        print("2. Retrieval Based on Codename")
        print("3. Retrieval Based on Specified RAM Capacity")
        print("4. Retrieval Based on Operating System\n")

        print("ANALYSIS:")
        print("5. Identify Top 5 Regions for a Brand")
        print("6. Analyze Average Price of Devices")
        print("7. Analyze Average Mass for Manufacturers")
        print("8. Display Least 5 Expensive Phones in Any Currency\n")

        print("VISUALIZATION:")
        print("9. Proportion of RAM Types")
        print("10. Number of Devices Per USB Type")
        print("11. Monthly Average Trends(GBP) for Devices")
        print("12. Relationship Between Display Diagonal and Pixel Density\n")

        print("0. Exit")

        try:

            choice = int(input("\nEnter your choice (0-12): \n"))
            if 0 <= choice <= 12:
                return choice
            else:
                print("Invalid choice. Please enter a number between 0 and 12.")

        except ValueError:
            print("Invalid input. Please enter a number.")

