# Задача 2
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения списка
#             или список задан изначально.
import os;
os.system('clear');

list_length = int (input("input list length - "));
nums = [i for i in range (1, list_length + 1)];
k = int (input ("input step to shift list - "));
# ниже формула позволяет оставляьть все значения в одном массиве копируя их
# и вставляет копию всех сначений в конце
# но с помощью срезов мы их меняем местами 
shift_nums = nums[k % list_length :] + nums [: k % list_length]   
shift_nums_1 = nums[:] + nums [:]   
print (nums)
print (shift_nums_1)
print (shift_nums)
print (nums[k % list_length :], nums [: k % list_length])

#  Метод второй
# так начало отсчета от 0 то (к - 1) но если сдвинуть на шаг 1 то сломается код 
# но код работает с остатком от (к % list_length)
for i in range (k % list_length):
    # по циклу ставит последний элемент списка на 0 место
    nums.insert(0, nums.pop(-1))
    print (nums)
print()
print(nums)
