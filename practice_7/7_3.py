# Задача 3
# Напишите функцию same_by(characteristic, objects),
# которая проверяет, все ли объекты имеют одинаковое
# значение некоторой характеристики, и возвращают True,
# если это так. Если значение характеристики для разных
# объектов отличается - то False. Для пустого набора объектов,
# функция должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same if same_by(lambda x: x % 2, values):
#     print(‘same’) 
# else:
#     print(‘different’)
import os;
os.system('clear')
def same_by (characteristic, obj):
    return len(set(map(characteristic, obj))) == 1
    # list_1 = list(map(characteristic, obj))
    # for i in range(len(list_1) - 1):
    #     if list_1[i] != list_1[i+1]:
    #         return False
    # else:
    #     return True

values = [0, 2, 10, 6]
print(same_by(lambda x: x % 2, values))
if same_by(lambda x: x%2, values):
    print ("same")
else:
    print ('different')