# Задача 3
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым.
# Напоминание: Простое число - это число, которое имеет 2
# делителя: 1 и n(само число)
# Input: 5 Output: yes
import os;
os.system('clear');
def prime_num (num):
    if num == 2:
        return True;
    elif num == 1 or num % 2 == 0:
        return False;
   
    for i in range (3, int((num ** 0.5) + 1), 2):
        if (num % 1 == 0):
            return False;
    return True;
print (prime_num(int(input ())))
        