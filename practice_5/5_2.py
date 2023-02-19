# Задача 2.
# Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но
# наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1
import os;
os.system('clear');
def change_val (marks):
    min_1 = min(marks);
    max_1 = max(marks);
    return [min_1 if i == max_1 else i for i in marks]
print(change_val([int(i) for i in input().split()]))
    