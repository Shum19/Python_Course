# Задача 2.
# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных
# символов идущих подряд, слова разделены одним или большим
# числом пробелов. Определите, сколько различных слов содержится
# в этом тексте.
# Input:  She sells sea shells on the sea shore The shells
#         that she sells are sea shells I'm sure.So if she 
#         sells sea shells on the sea shore I'm sure that the shells 
#         are sea shore shells
# Output: 13
import os;
os.system('clear');
text = input("Type your text below\n").replace('.', ' ').lower().split();
new_set = set(i for i in text)
# for i in text:
#     new_set.add(i);
print (new_set);
print (len(new_set));

