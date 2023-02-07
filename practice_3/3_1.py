#  Задача 1.
# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6
# Примечание: Пользователь может вводить значения списка
#             или список задан изначально.
nums = [];
list_length = int (input("input list length - "))
count = 0;
for i in range (list_length):
    digit = int (input (f"Input number {i+1} - "))
    nums.append(digit)

nums_of_diction = set (nums)
print (nums_of_diction)
print (len(nums_of_diction))
        
    
