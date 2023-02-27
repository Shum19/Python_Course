# Задача 1 Винни-Пух попросил Вас посмотреть, есть ли в его
# стихах ритм. Поскольку разобраться в его кричалках не настолько
# просто, насколько легко он их придумывает, Вам стоит написать
# программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке
# Ввод:                                       Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам      Парам пам-пам
import os;
os.system('clear')
def true_rythm (str_1):
    list_1 = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'э', 'ю', 'я', 
              'А', 'Е', 'Ё', 'И', 'Й', 'О', 'У', 'Э', 'Ю', 'Я']
    str_list = str_1.split()
    vowel_list = []
    count = 0
    for i in range(len(str_list)):
        count = 0
        for j in str_list[i]:
            if j in list_1:
                count += 1
        vowel_list.append(count)
    if all(vowel_list):
        return 'Парам пам-пам'
    else:
        return 'Парам' 

test = true_rythm(input())
print(test)