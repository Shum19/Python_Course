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
import os
from os import path
file_base = "phone_book_base.txt"
new_file_base = 'copied_phone_book.txt'
file_for_export = 'phone_book_for_export.txt'
all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_records():
    global id, all_data
    with open(file_base) as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0])
        return all_data

# option 1 show all contact
def show_all():
    read_records()
    print(*all_data, sep=', ')

# option 2 add contact
def add_new_contact():
    global id
    read_records()
    if all_data:
        id = int(all_data[-1][0])
    contact_list = ['Sername', 'Name', 'Second Name', 'Phone Number']
    contact = ''
    for i in contact_list:
        contact += input(f'Enter {i} ') + ' '
    id +=1
    with open(file_base, 'a', encoding='utf-8') as f:
        f.write(f'{id} {contact}\n')

# option 3 search contact
def search_contact():
    read_records()
    global searched_list
    rqwrd_contact = input(f'Enter contact - ').lower()
    searched_list = []
    for contact in all_data:
        if rqwrd_contact in contact.lower():
            searched_list.append(contact)
    return searched_list

# option 4 delete contact
def delete_contact():
    global deleted_contact
    read_records()
    search_contact()
    print(*searched_list, sep='\n')
    id_1 = input('Enter Contact ID to delete - ')
    pop_index = 0
    for i in range(len(all_data)):
        if all_data[i][0] == id_1:
            pop_index = i
            deleted_contact = all_data[i]
    all_data.pop(pop_index)
    id = 0
    with open(file_base, 'w', encoding='utf-8') as f:
        for contact in all_data:
            id = int(id) + 1
            contact = contact[2:]
            f.write(f'{id} {contact}\n')
    read_records()
    return all_data

# option 5 change contact
def change_contact():
    read_records()
    search_contact()
    print(*searched_list, sep='\n')
    id_2 = input('Enter Contact ID to change - ')
    change_index = 0
    for i in range(len(all_data)):
        if id_2 == all_data[i][0]:
            change_index = i
    contact = all_data[change_index][2:].split()
    contact_list = ['1. Sername', '2. Name', '3. Second Name', '4. Phone Number']
    for item in range(len(contact_list)):
        print(contact_list[item], contact[item])
    contact = all_data[change_index]
    choice = input('Choose digit 1 - 4 to change item - ')
    if choice == '1':
        contact = contact.split(' ')
        old_surname = contact[1]
        contact[1] = input('Enter new Surname - ')
        contact = ' '.join(contact)
        print(f"Old Surname {old_surname}\n"
              f"New Surname {contact} saved\n")

    elif choice == '2':
        contact = contact.split(' ')
        old_name = contact[2]
        contact[2] = input('Enter new Name - ')
        contact = ' '.join(contact)
        print(f"Old Name {old_name}\n"
              f"New Name {contact} saved\n")

    elif choice == '3':
        contact = contact.split(' ')
        old_second_name = contact[3]
        contact[3] = input('Enter new Second Name - ')
        contact = ' '.join(contact)
        print(f"Old Second Name {old_second_name}\n"
              f"New Second Name {contact} saved\n")

    elif choice == '4':
        contact = contact.split(' ')
        old_number = contact[4]
        contact[4] = input('Enter new Phone number - ')
        contact = ' '.join(contact)
        print(f"Old Phone Number {old_number}\n"
              f"New Phone Number {contact} saved\n")

    all_data[change_index] = contact
    with open(file_base, 'w', encoding='utf-8') as f:
        for item in all_data:
            f.write(f'{item}\n')

# option 6
def export_contact():
    with open(new_file_base, 'w', encoding='utf-8') as f_new, open(file_base, 'r') as f_old:
        for contact in f_old:
            f_new.write(contact)


# option 7 import phone_book
def import_contact():
    global all_data
    read_records()
    with open(file_for_export) as f_export:
        export_data = [i.strip() for i in f_export]
        export_data = [i[2:] for i in export_data]
        all_data = [j[2:] for j in all_data]
        all_data_set = set(all_data)
        export_set = set(export_data)
        updated_list = list(export_set.difference(all_data_set))
        read_records()
        with open(file_base, 'a', encoding='utf-8') as f_added:
            id = int(all_data[-1][0])
            for added_contact in updated_list:
                id += 1
                f_added.write(f'{id} {added_contact}\n')

def main_menu ():
    play = True
    while play:
        answer = input("\nPhone Book\n"
                  "1. Show all\n"
                  "2. Add new contact\n"
                  "3. Search contact\n"
                  "4. Delete contact\n"
                  "5. Change contact\n"
                  "6. Export contacts\n"
                  "7. Import contacts\n"
                  "8. Exit\n")
        if answer == "1":
            show_all()
        elif answer == "2":
            add_new_contact()
            read_records()
            print(f'New contact was created - {all_data[-1]}')
        elif answer == "3":
            search_contact()
            print(*searched_list, sep='\n')
        elif answer == "4":
            delete_contact()
            print(f'Contact was deleted - {deleted_contact}')
        elif answer == "5":
            change_contact()
        elif answer == '6':
            export_contact()
            dir = os.path.abspath(new_file_base)
            print(f'Your copy saved in this path {dir}\nAnd Name is {new_file_base}')
        elif answer == '7':
            import_contact()
            print('All contacts were imported ')
        elif answer == "8":
            play = False
        else:
            print('Try again\n')
main_menu()