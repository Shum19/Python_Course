# Задача 3 В настольной игре Скрабл (Scrabble) каждая
# буква имеет определенную ценность. В случае с английским
# алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость
# введенного пользователем слова. Будем считать,
# что на вход подается только одно слово, которое содержит
# либо только английские, либо только русские буквы.
# Ввод: ноутбук Вывод: 12
import os;
os.system('clear');
import random;

# Код для создания словарей то есть копируем набор букв в задании 
# и с каждой итерацаиией убераем зяпятуюю и пробел ии создаем первый список
# с ключами далее создаем список словарей с ключем который тоже вводим
# и результат получается как dict_list_ru или dict_list_en 
# list = [input().replace(', ', '') for i in range(7)]
# # list = ['АВЕИНОРСТ', 'ДКЛМПУ', 'БГЁЬЯ', 'ЙЫ', 'ЖЗХЦЧ', 'ШЭЮ', 'ФЩЪ']
# list_list = []
# for i in range(len(list)):
#     diction = {list[i] : int(input())}
#     list_list.append(diction)
# print (list_list)
dict_list_ru = [{'АВЕИНОРСТ': 1}, {'ДКЛМПУ': 2}, 
             {'БГЁЬЯ': 3}, {'ЙЫ': 4}, {'ЖЗХЦЧ': 5}, 
             {'ШЭЮ': 8}, {'ФЩЪ': 10}]
dict_list_en = [{'AEIOULNSTR': 1}, {'DG': 2}, {'BCMP': 3}, 
                {'FHVWY': 4}, {'K': 5}, {'JX': 8}, {'QZ': 10}]
choose_lang = input("Choose language typing en or ru - ").lower()
if choose_lang == "en":
    word = input("Type your word - ")
    word = word.upper()
    word_list = [word[i] for i in range (len(word))]
    count = 0
    for i in range(len(dict_list_en)):#цикл который берет всю длину списка словаря
        for key in dict_list_en[i]:#цикл который берет перывй словарь
            val = list(dict_list_en[i].values())[0]#вытаскиваем значение по ключу типа int
            for letter in range (len(word_list)):#цикл который листает буквы в слове
                for letter_key in range (len(key)):#цикл который листает буквы в ключе словаря
                    if word_list [letter] == key[letter_key]:#сравнивает буквы слова и ключа в словаре
                        count += val#если выше иистина то сичает очки по значения ключа
    print(count)
else:
    if choose_lang == "ru":
        word = input("Type your word - ")
        word = word.upper()
        word_list = [word[i] for i in range (len(word))]
        count = 0
        for i in range(len(dict_list_ru)):
            for key in dict_list_ru[i]:
                val = list(dict_list_en[i].values())[0]
                for letter in range (len(word_list)):
                  for letter_key in range (len(key)):
                      if word_list [letter] == key[letter_key]:
                        count += val
    print (count)


