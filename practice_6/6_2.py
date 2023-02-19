# Задача 2
# Дан массив, состоящий из целых чисел. Напишите программу, 
# которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента 
# меньше данного. Сначала вводится число N — количество 
# элементов в массиве Далее записаны N чисел — элементы массива. 
# Массив состоит из целых чисел.
# Ввод:                   Ввод:
# 5                       5
# 1 2 3 4 5               1 5 1 5 1
# Вывод:                  Вывод:
# 0                       2
import os;
os.system('clear');
array = list(map(int, input('Input a list of nums - ').split()));
length = len(array) - 1;
count = 0;
for i in range (1, length):
    if array[i] == max(array[i - 1 : i + 2]):
        count += 1;
print(count)
#  second method
print (len([i for i in range(1, length) if array[i] == max(array[i - 1 : i + 1])]))
