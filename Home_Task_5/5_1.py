# Задача 1 Напишите программу, которая на вход принимает два 
# числа A и B, и возводит число А в целую степень B с помощью
# рекурсии.
# A = 3; B = 5 -> 243 (35) 
# A = 2; B = 3 -> 8
import os;
os.system('clear');
def paw_num(num_a, num_b):
    if num_b == 0:
        return 1;
    return (num_a * paw_num(num_a, num_b - 1))
print (paw_num(int(input("Base - ")), int(input("Power - "))))