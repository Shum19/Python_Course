# Задача 4
# Дано натуральное число N и последовательность из
# N элементов. Требуется вывести эту последовательность
# в обратном порядке. Примечание. В программе запрещается
# объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4 Output: 4 3
import os;
os.system('clear');
def reverse_list(num):
    if num == 0:
        return "";
    list_1 = input();
    return reverse_list(num - 1) + f"{list_1} "
print(reverse_list(int(input())))
