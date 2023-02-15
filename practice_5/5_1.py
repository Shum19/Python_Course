# Задача 1
# Последовательностью Фибоначчи называется последовательность чисел 
# a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7 Output: 21
import os;
os.system('clear');
def fib(num):
    if num <= 1:
        return 1
    return fib(num - 1) + fib(num - 2)
# print(list_fib[fib(7)] for i in range(7)])
    
    
    
