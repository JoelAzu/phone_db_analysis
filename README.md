# phone_db_analysis
Software program to retrieve, analyse and visualize from a given database. 

Introduction
PhoneDB website, which is the information website for smartphones, tablets, PDAs, and mobile devices. PhoneDB offers a comprehensive collection of data and various services that harness the potential of this valuable resource to aid users in finding the most suitable mobile device.

The data file, device_features.csv, contains 48 columns. Each row in the file represents a single record for a device. The data set contains complete data for all columns for each record in the file. 

Requirements
The requirements for the system are as follows:
a)
The system will allow the user to retrieve data from a CSV file using the csv module and fundamental python (control structure and file processing) to perform the following:
-
Load the data from a CSV file into memory using the csv reader function. The path to the file will be specified by the user then use these loaded data to perform following tasks:
a1.
Retrieve the model name, manufacturer, weight, price, and price currency for the device(s) based on the oem_id.
a2.
Retrieve the brand, model name, RAM capacity, market regions, and the date when the information was added for device(s) associated with a specified code name.
a3.
Retrieve the oem_id, release date, announcement date, dimensions, and device category of the device(s) based on a specified RAM capacity.
a4.
Retrieve information from your chosen columns and apply a specific condition that relates to an individual device. Please select at least three columns and one condition that differs from previous requirements.

b)
The system will allow the user to analyse/query data using the pandas module to perform the following:
-
Load data from a CSV file into memory using the pandas module. Use the file path received from task a) for this purpose. After loading the data, proceed with the following tasks.
b1.
Identify the top 5 regions where a specific brand of devices was sold.
b2.
Analyse the average price of devices within a specific brand, all in the same currency.
b3.
Analyse the average mass for each manufacturer and display the list of average mass for all manufacturers.
b4.
Analyse the data to derive meaningful insights based on your unique selection, distinct from the previous requirements.

c)
The system will allow the user to visualise the data using the matplotlib module as follows:
-
Load data from a CSV file into memory. Use the file path received from task a) for this purpose. After loading the data, proceed with the following tasks.
c1.
Create a chart to visually represent the proportion of RAM types for devices in the current market.
c2.
Create a chart to visually compare the number of devices for each USB connector type
c3.
Create separate charts illustrating the monthly average price trends (in GBP) for devices released in each year from 2020 to 2023. Each chart should focus on a specific year.
c4.
Create a visualisation of your selection to showcase information related to device features that can reveal trends, behaviours, or patterns, ensuring it is distinct from previous requirements.
