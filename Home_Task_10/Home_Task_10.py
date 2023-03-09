# -*- coding: utf-8 -*-

# -- Sheet --


# sklearn.preprocessing import OneHotEncoder
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
print (lst)
df = pd.DataFrame({'whoAmI':lst})
df
# первое это тест get_dummies на вывод и второе это решение той же задачи и вывод такой же таблицы без использования get_dummies

pd.get_dummies(df['whoAmI'])

# решениие задачи бес использования get_dummies
human_list = []
robot_list = []
print (lst)
for i in lst:
    if i =='human' in lst:
        human_list.append(1)
    else:
        human_list.append(0)
for j in lst:
    if j == 'robot':
        robot_list.append(1)
    else:
        robot_list.append(0)
df_encoded = pd.DataFrame({'human':human_list, 'robot':robot_list})
df_encoded


