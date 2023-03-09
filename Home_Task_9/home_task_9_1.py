# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
df = pd.read_csv('california_housing_train.csv')

# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
round(df.loc[(df['population'] >= 0)&(df['population'] <= 500), 'median_house_value'].mean(), 2)

# Узнать какая максимальная households в зоне минимального значения population
df.loc[df['population'] == df['population'].min(), 'households'].max()

df[df['population'] == df['population'].min()].index

df.iloc[[8232]]

df[(df['population'] >= 0)&(df['population'] <= 500)]['population']

