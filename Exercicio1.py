import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sales = pd.read_csv(
    'data/sales_data.csv',
    parse_dates=['Date'])

sales.head()

var = sales.shape

sales.info()

sales.describe()

sales['Unit_Cost'].describe()

sales['Unit_Cost'].mean()

sales['Unit_Cost'].median()
sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14, 6))
# sales['Unit_Cost'].plot(kind='density', figsize=(14, 6))

ax = sales['Unit_Cost'].plot(kind='box', figsize=(14, 6))
ax.axvline(sales['Unit_Cost'].mean(), color='red')
ax.axvline(sales['Unit_Cost'].median(), color='green')

ax = sales['Unit_Cost'].plot(kind='hist', figsize=(14, 6))
ax.set_ylabel('Number of Sales')
ax.set_xlabel('dollars')

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

corr = sales.corr()

fig = plt.figure(figsize=(8, 8))
plt.matshow(corr, cmap='RdBu', fignum=fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical')
plt.yticks(range(len(corr.columns)), corr.columns)

sales.plot(kind='scatter', x='Customer_Age', y='Revenue', figsize=(6, 6))

sales.plot(kind='scatter', x='Revenue', y='Profit', figsize=(6, 6))

ax = sales[['Profit', 'Age_Group']].boxplot(by='Age_Group', figsize=(10, 6))
ax.set_ylabel('Profit')

sales['Revenue'] += 50
var = sales.loc[(sales['Country'] == 'Canada') | (sales['Country'] == 'France')].shape[0]
var = sales.loc[(sales['Country'] == 'Canada') & (sales['Sub_Category'] == 'Bike Racks')].shape[0]
france_states = sales.loc[sales['Country'] == 'France', 'State'].value_counts()

sales['Revenue_per_Age'] = sales['Revenue'] / sales['Customer_Age']

sales['Revenue_per_Age'].head()

# sales['Revenue_per_Age'].plot(kind='density', figsize=(14, 6))

france_states.plot(kind='bar', figsize=(14, 6))
sales['Product_Category'].value_counts()
sales['Product_Category'].value_counts().plot(kind='pie', figsize=(6, 6))
accessories = sales.loc[sales['Product_Category'] == 'Accessories', 'Sub_Category'].value_counts()

sales['Calculated_Cost'] = sales['Order_Quantity'] * sales['Unit_Cost']

sales['Calculated_Cost'].head()

(sales['Calculated_Cost'] != sales['Cost']).sum()

accessories.plot(kind='bar', figsize=(14, 6))
bikes = sales.loc[sales['Product_Category'] == 'Bikes', 'Sub_Category'].value_counts()

sales.plot(kind='scatter', x='Calculated_Cost', y='Profit', figsize=(6, 6))

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

sales['Revenue'].plot(kind='hist', bins=100, figsize=(14, 6))

sales['Unit_Price'].head()
sales['Unit_Price'] *= 1.03
sales['Unit_Price'].head()
