# Задача 1 
# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3 -> 1
import os;
os.system('clear');
import random;

list_length = int(input("Input length of list - "))
list = [random.randrange(1, 5) for i in range(list_length)]
print(list)
x_find = int(input ("Input digit you want to find in list - "))
print (f"The {x_find} - {list.count(x_find)} times")