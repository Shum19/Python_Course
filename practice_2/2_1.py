# Задача 1
# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 
# 0! = 1 Решить задачу используя цикл while
# Input: 5 Output: 120

digit = int (input("Input factoriial number\n"));
factorial = 1;
showFact = digit;
# if digit == 0:
#     print (f"{digit}! = 1");
# else:
while digit > 0:
        factorial *= digit;
        digit -=1;
print (f"{showFact}! = {factorial}");