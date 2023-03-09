# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
df = pd.read_csv('california_housing_test.csv')

df.shape 

df.dtypes

# Проверить есть ли в файле пустые значения
df.isnull().sum()

# Показать median_house_value где median_income < 2
# df[df['median_income'] < 2]['median_house_value']
df.loc[df['median_income'] < 2, 'median_house_value']

# Показать данные в первых 2 столбцах longitude, latitude
df[['longitude', 'latitude']]

# Выбрать данные где housing_median_age < 20 и median_house_value > 70000
df.loc[(df['housing_median_age']< 20)&(df['median_house_value'] > 7000)]

# Определить какое максимальное и минимальное значение median_house_value
df['median_house_value'].max()

# Определить какое максимальное и минимальное значение median_house_value
df['median_house_value'].min()

# Показать максимальное median_house_value, где median_income = 3.1250
df.loc[df['median_income'] == 3.1250, 'median_house_value'].max()

# Узнать какая максимальная population в зоне минимального значения median_house_value
df.loc[df['median_house_value'] == df['median_house_value'].min(), 'population'].max()

