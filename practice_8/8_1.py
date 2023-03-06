# Задача 1
# Создать телефонный справочник с возможностью импорта и экспорта данных
# в формате .txt. Фамилия, имя, отчество, номер телефона - данные,
# которые должны находиться в файле.
# 1.  Программа должна выводить данные
# 2.  Программа должна сохранять данные в
#     текстовом файле
# 3.  Пользователь может ввести одну из
#     характеристик для поиска определенной записи
#     (Например имя или фамилию человека)
# 4.  Использование функций. Ваша программа не должна быть линейной
from os import path
import os
os.system('clear')

file_base = "base.txt";
all_data = []
id = 0;

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass
    
def read_records():
    global all_data, id
    with open(file_base) as f:
        all_data = [i.strip() for i in f];
        if all_data:
            id = int(all_data[-1][0])
        return all_data;

def show_all():
    read_records()
    print(*all_data, sep="\n")

def add_records ():
    read_records()
    global id;
    list_1 = ['Surname', 'Name', 'Second Name', 'Phone Number'];
    string = '';
    for i in list_1:
        string += input(f'Enter {i} ') + ' ';
    id +=1;
    with open(file_base, 'a', encoding='utf-8') as f:
        f.write(f"\n{id} {string}\n" )

def search_contact():
    read_records()
    item = input('Enter: Surname, Name, Second Name, Phone Namber - ').lower()
    found = [(i for i in all_data for j in list(i.split()) 
              if item.lower() == j.lower())]
    if found:
        print(*found, sep='\n')
    else:
        print('Not Found'.upper())
    return found
 
def delete_contact():
    pass;



def main_menu ():
    play = True;
    while play:
        answer = input("\nPhone Book:\n"
                        "1. Show all records\n"
                        "2. Add records\n"
                        "3. Search records\n"
                        "4. Delete number\n"
                        "5. Change number\n"
                        "6. Exit\n");
        if answer == "1":
            show_all();
        elif answer == "2":
            add_records();
        elif answer == "3":
            search_contact();   
        elif answer == "4":
            pass;
        elif answer == "5":
            pass;
        elif answer == "6":
            play = False;
        else: 
            print('Try again\n')

# main_menu()   
# print (add_records()) 
# show_all()

       