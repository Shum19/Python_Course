# Задача 2
# Дано натуральное число A > 1. Определите, каким по счету
# числом Фибоначчи оно является, то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5 Output: 
resultOfFibbonachi = int(input ("Input the Fibbonacci result\n"));
a = 0;
b = 1;
count = 2;
while b <= resultOfFibbonachi:
    # print (a, b)
    if b == resultOfFibbonachi:
        print (count);
        break;
    (a, b) = (b, a + b);
    count += 1;
else:
    print (-1);