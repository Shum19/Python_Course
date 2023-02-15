# Задача 2 Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2, 2 -> 4
import os;
os.system('clear');
def sum (num_a, num_b):
    if num_b == 0:
        return num_a;
    return sum(num_a + 1, num_b - 1);
print (sum(int(input()), int(input())))