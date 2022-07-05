# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 02:58:03 2022

@author: sayon
"""

import pandas as pd

#file_name = pd.read_csv('file.csv') <-- format of read_csv
data = pd.read_csv('transaction.csv')
data = pd.read_csv('transaction.csv',sep=';')

#summary of the data
data.info()

#Working with Calculation
#Defining Variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathematical Operations

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = (SellingPricePerItem - CostPerItem)*NumberOfItemsPurchased
CostPerTransaction = NumberOfItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem

#CostPerTransaction Column Calculation 
#CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#Variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#Adding a new column to dataframe

data['CostPerTransaction'] = data['CostPerItem']*data['NumberOfItemsPurchased']


#SalesPerTransaction Column
data['SalesPerTransaction'] = data['SellingPricePerItem']*data['NumberOfItemsPurchased']


#ProfitPerTransaction Column
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']


#MarkupPerTransaction Column = (Sales - Cost)/Cost
data['Markup'] = data['ProfitPerTransaction']/data['CostPerTransaction']

#Rounding markup
roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

#Combining data fields

my_date = 'Day'+'-'+'Month'+'-'+'Year'

#my_date = data['Day']+'-'+data['Month']+'-'+data['Year']
##The above did not work so we do the following

#checking columns data_type
print(data['Day'].dtype)
print(data['Year'].dtype)

#Change column types
day = data['Day'].astype(str)
print(day.dtype)

year = data['Year'].astype(str)
print(year.dtype)

# Again back to combining data fields
my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date

#using split to split the client keywords field
#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#create new columns for the splitted column in client keyword
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#using the replace function to remove the square brackets and quotes from the splitted cells above
data['ClientAge'] = data['ClientAge'].str.replace('[','', regex=True)
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','', regex=True)

data['ClientAge'] = data['ClientAge'].str.replace("'",'')
data['ClientType'] = data['ClientType'].str.replace("'",'')
data['LengthOfContract'] = data['LengthOfContract'].str.replace("'",'')

#Changing item description to lower case
data['ItemDescription'] = data['ItemDescription'].str.lower()

#Bringing in a new dataset
seasons = pd.read_csv('value_inc_seasons.csv' , sep =';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')
data = pd.merge(data, seasons, on = 'Month')


#dropping some fields that are not needed
#df = df.drop('columnname', axis = 1)
data = data.drop('ClientKeywords', axis = 1)
data = data.drop(['Day','Year','Month'], axis = 1)

#Export into CSV
data.to_csv('ValueInc_Cleaned.csv', index = False)
