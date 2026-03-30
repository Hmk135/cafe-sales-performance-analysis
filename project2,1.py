import pandas as pd
df = pd.read_csv("D:/SERIOUS/Project2/dirty_cafe_sales.csv")
df = df.set_index("Transaction ID")

df['Quantity'] = pd.to_numeric(df['Quantity'],errors = 'coerce')
df['Total Spent'] = pd.to_numeric(df['Total Spent'],errors = 'coerce')
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'],errors = 'coerce')

mask_TS = df['Price Per Unit'].notna() & df['Quantity'].notna() & df ['Total Spent'].isna()
df.loc[mask_TS,'Total Spent'] = (df.loc[mask_TS,'Price Per Unit'] * df.loc[mask_TS,'Quantity'])

mask_PPU = df['Price Per Unit'].isna() & df['Quantity'].notna() & df['Total Spent'].notna()
df.loc[mask_PPU,'Price Per Unit'] = (df.loc[mask_PPU,'Total Spent'] / df.loc[mask_PPU,'Quantity'])

mask_Q = df['Quantity'].isna() & df['Total Spent'].notna() & df['Price Per Unit'].notna()
df.loc[mask_Q,'Quantity'] = (df.loc[mask_Q,'Total Spent'] / df.loc[mask_Q,'Price Per Unit'])
print(df.groupby('Item')['Price Per Unit'].unique())

price_map = df.groupby('Item')['Price Per Unit'].median()
df.loc[df['Price Per Unit'].isna(),'Price Per Unit'] = df.loc[df['Price Per Unit'].isna() ,'Item'].map(price_map)

df['Total Spent'] = df['Price Per Unit'] * df['Quantity']
print(df['Total Spent'].sum())

total_spent_each = df.groupby('Item')['Total Spent'].sum()
doanh_thu_sap_xep = total_spent_each.sort_values(ascending=False)
print(doanh_thu_sap_xep)

total_buy = df.groupby('Item')['Quantity'].sum()
hot_stuff = total_buy.sort_values(ascending=False)
print(hot_stuff.head(5))
print(df['Payment Method'].value_counts(dropna=False))
print(df['Location'].value_counts(dropna=False))

import numpy as np

df['Payment Method'] = df['Payment Method'].replace(['ERROR', 'UNKNOWN'], np.nan)
df['Location'] = df['Location'].replace(['ERROR', 'UNKNOWN'], np.nan)

df['Payment Method'] = df['Payment Method'].fillna('Not Specified')
df['Location'] = df['Location'].fillna('Not Specified')

df['Item'] = df['Item'].replace(['ERROR', 'UNKNOWN'], np.nan)
df = df.dropna(subset=['Item'])

df.info()
print(df.head())
print(df.describe())
print(df.isnull().sum())

df.to_csv('clean_cafe_sales.csv')

