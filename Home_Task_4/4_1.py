# Задача 22
# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.Пользователь вводит 2 числа.
# n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# n = 11, m = 6
# {2 4 6 8 10 12 10 8 6 4 2}
# {3 6 9 12 15 18}
# {6 12}
import os, random;
os.system('clear')

n = int(input("Type n quantities - "));
m = int(input("Type m quantities - "));
first_set = set(random.randint(0, 10) for i in range(n))
second_set = set(random.randint(0, 10) for i in range(m))
# first_set = set([2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2])
# second_set = set([3, 6, 9, 12, 15, 18])
print(first_set)
print (second_set)
show_interc = first_set.intersection(second_set)
show_interc = list(show_interc)
show_interc.sort()
print(show_interc)

