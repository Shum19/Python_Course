# Задача 3
# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
#         {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
import os;
os.system('clear');

list_of_diction = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
                   {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, 
                   {" VIII ":" S007 "}];
list_2 = [];
print(type(set))
for i in list_of_diction:
    new_list = list(i.values())[0].strip()
    list_2.append(new_list)
print(len(list_2))
print (set(list_2))
# Method 2
print (set (list (i.values())[0].strip() for i in list_of_diction))
