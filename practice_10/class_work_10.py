# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
import seaborn as sns

df = pd.read_csv('california_housing_train.csv')

# Изобразите отношение households к population с помощью точечного графика
sns.scatterplot(data=df, x="households", y="population")

# Визуализировать longitude по отношения к median_house_value, используя линейный график
sns.lineplot(x="longitude", y="median_house_value", data=df)

sns.relplot(x="longitude", y="median_house_value", kind="line", data=df)

# Представить гистограмму по housing_median_age
sns.histplot(data=df, x="housing_median_age")

# Изобразить гистограмму по median_house_value с оттенком housing_median_age

# sns.displot(x='median_house_value', hue='housing_median_age', data = df)
sns.histplot(data=df, x="median_house_value", hue='housing_median_age')

# # Пингвины


penguins = sns.load_dataset("penguins")
penguins.head()

# Использовать 2-3 точечных графика
# style есть darkgrid, whitegrid, dark, white, ticks

sns.set(style="ticks")
sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='sex', size=5)

# Использовать 2-3 точечных графика
sns.set(style="darkgrid")
sns.scatterplot(data=penguins, x='body_mass_g', y='flipper_length_mm', hue='sex', size=6)

# Использовать 2-3 точечных графика
sns.set(style="whitegrid")
sns.scatterplot(data=penguins, x='body_mass_g', y='flipper_length_mm', hue='sex', size=6)

# Использовать PairGrid с типом графика на ваш выбор
# Изобразить Heatmap

cols = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']
g = sns.PairGrid(penguins[cols])
g.map(sns.scatterplot)

# Использовать 2-3 гистограммы
sns.histplot(data=penguins, x='bill_depth_mm')

# Использовать 2-3 гистограммы
sns.histplot(data=penguins, x='bill_length_mm')

# Использовать 2-3 гистограммы
sns.histplot(data=penguins, x='flipper_length_mm')

# # Столбец


# Создать новый столбец в таблице с пингвинами, который будет отвечать  за показатель длины клюва пингвина.
# high - длинный(от 42)
# middle - средний(от 35 до 42)
# low - маленький(до 35)
penguins.loc[penguins['bill_length_mm'] < 35, 'beak_length'] = 'low'
penguins.loc[(penguins['bill_length_mm'] > 34) & (penguins['bill_length_mm'] < 42), 'beak_length'] = 'middle'
penguins.loc[penguins['bill_length_mm'] >= 42, 'beak_length'] = 'high'

penguins

# # Гистограмма


# Изобразить гистограмму по flipper_length_mm с оттенком height_group. Сделать анализ
# sns.histplot(data=penguins, x="flipper_length_mm", hue='beak_length')
sns.displot(penguins, x="flipper_length_mm", hue="beak_length")

