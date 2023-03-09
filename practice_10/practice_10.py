# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
import seaborn as sns
df = pd.read_csv('california_housing_test.csv')

# Изобразите отношение households к population с
# помощью точечного графика
sns.scatterplot(x = 'households', y = 'population', data=df)

df.columns

# Визуализировать longitude по отношения к median_house_value, используя линейный график
sns.lineplot(x='longitude', y='median_house_value', data=df)

# Представить гистограмму по housing_median_age
sns.histplot(x='housing_median_age', data=df)

# Изобразить гистограмму по median_house_value с
# оттенком housing_median_age
sns.histplot(data=df, x= 'median_house_value', hue='housing_median_age')

penguins = sns.load_dataset("penguins")
penguins.columns

# Использовать 2-3 точечных графика
# Применить доп измерение в точечных графиках, используя
# аргументы hue, size, stile
sns.set(style='darkgrid')
sns.scatterplot(data=penguins, x= 'bill_length_mm', y= 'bill_depth_mm', hue= 'sex', size=5)

# Использовать PairGrid с типом графика на ваш выбор
columns = ['species', 'island','bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g','sex']
g = sns.PairGrid(penguins[columns])
g.map(sns.scatterplot)

# Изобразить Heatmap
sns.histplot(data=penguins, x= 'body_mass_g')

#  Создать новый столбец в таблице с пингвинами, который будет отвечать за
#  показатель длины клюва пингвина.
#  high - длинный(от 42)
#  middle - средний(от 35 до 42)
#  low - маленький(до 35)
penguins.loc[penguins['bill_length_mm'] < 35, 'bill_size'] = 'low'
penguins.loc[(penguins['bill_length_mm'] >= 35)&(penguins['bill_length_mm']) < 42, 'bill_size'] = 'middle'
penguins.loc[penguins['bill_length_mm'] >= 42, 'bill_size'] = 'high'
penguins

# Изобразить гистограмму по flipper_length_mm с оттенком height_group. Сделать анализ
sns.histplot(data= penguins, x= 'flipper_length_mm', hue='bill_size')

sklearn.preprocessing import OneHotEncoder

