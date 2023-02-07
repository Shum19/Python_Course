# Задача 2
# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь
# в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих строках записаны N
# целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6 -> 5
import os;
os.system('clear');
import random;

list_length = int(input("Input length of list - "))
list = [random.randrange(-8, 9) for i in range(list_length)]
print(list)
x_find = int (input ("Input digit - "))
min = list[0] - x_find if list[0] - x_find >= 0 else x_find - list[0]
for i in range (0, list_length):
    temp = list[i] - x_find if list[i] - x_find >= 0 else x_find - list[i]
    if temp < min:
        min = temp
        result = list[i]
        
print (result)
