import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sales = pd.read_csv(
    'data/sales_data.csv',
    parse_dates=['Date'])

sales.head()
sales['Customer_Age'].mean()
sales['Customer_Age'].plot(kind='box', vert=False, figsize=(14, 6))
sales['Year'].value_counts()
sales['Year'].value_counts().plot(kind='bar', figsize=(6, 6))
sales['Month'].value_counts()
sales['Month'].value_counts().plot(kind='bar', figsize=(14, 6))
sales['Country'].value_counts().head(1)
sales['Country'].value_counts()
sales['Country'].value_counts().plot(kind='bar', figsize=(14, 6))
sales['Product'].unique()
sales['Product'].value_counts().head(10).plot(kind='bar', figsize=(14, 6))
sales.plot(kind='scatter', x='Unit_Cost', y='Unit_Price', figsize=(6, 6))
sales.plot(kind='scatter', x='Order_Quantity', y='Profit', figsize=(6, 6))
sales[['Profit', 'Country']].boxplot(by='Country', figsize=(10, 6))
sales[['Customer_Age', 'Country']].boxplot(by='Country', figsize=(10, 6))
sales['Calculated_Date'] = sales[['Year', 'Month', 'Day']].apply(lambda x: '{}-{}-{}'.format(x[0], x[1], x[2]), axis=1)

sales['Calculated_Date'].head()

sales['Calculated_Date'] = pd.to_datetime(sales['Calculated_Date'])

sales['Calculated_Date'].head()
sales['Calculated_Date'].value_counts().plot(kind='line', figsize=(14, 6))
sales['Revenue'] += 50
var = sales.loc[(sales['Country'] == 'Canada') | (sales['Country'] == 'France')].shape[0]
var = sales.loc[(sales['Country'] == 'Canada') & (sales['Sub_Category'] == 'Bike Racks')].shape[0]
france_states = sales.loc[sales['Country'] == 'France', 'State'].value_counts()


france_states.plot(kind='bar', figsize=(14, 6))
sales['Product_Category'].value_counts()
sales['Product_Category'].value_counts().plot(kind='pie', figsize=(6, 6))
accessories = sales.loc[sales['Product_Category'] == 'Accessories', 'Sub_Category'].value_counts()


accessories.plot(kind='bar', figsize=(14, 6))
bikes = sales.loc[sales['Product_Category'] == 'Bikes', 'Sub_Category'].value_counts()


bikes.plot(kind='pie', figsize=(6, 6))
sales['Customer_Gender'].value_counts()
sales['Customer_Gender'].value_counts().plot(kind='bar')
var = sales.loc[(sales['Customer_Gender'] == 'M') & (sales['Revenue'] == 500)].shape[0]

sales.sort_values(['Revenue'], ascending=False).head(5)
cond = sales['Revenue'] == sales['Revenue'].max()

var = sales.loc[cond]
cond = sales['Revenue'] > 10_000

sales.loc[cond, 'Order_Quantity'].mean()
cond = sales['Revenue'] < 10_000

sales.loc[cond, 'Order_Quantity'].mean()
cond = (sales['Year'] == 2016) & (sales['Month'] == 'May')

var = sales.loc[cond].shape[0]
cond = (sales['Year'] == 2016) & (sales['Month'].isin(['May', 'June', 'July']))

# sales.loc[cond].shape[0]
profit_2016 = sales.loc[sales['Year'] == 2016, ['Profit', 'Month']]

profit_2016.boxplot(by='Month', figsize=(14, 6))
sales.loc[sales['Country'] == 'United States', 'Unit_Price'] *= 1.072
