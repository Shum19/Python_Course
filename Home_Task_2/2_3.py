# Задача 3
# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8
import os;
os.system('clear')

number = int (input ("Input number - "));
count = 2;
for i in range(number):
    count = count ** i;
    if count >= number:
        break;
    print (count);
    count = 2;
    