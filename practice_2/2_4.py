# Задача 4
# Иван Васильевич пришел на рынок и решил купить два арбуза:
# один для себя, а другой для тещи. Понятно, что для себя 
# нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот
# незадача: арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему! Пользователь вводит
# одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса
# соответствующего арбуза
# Input: 5 -> 5 1 6 5 9 Output: 1 9
import os;
os.system('clear');
q_watermelon = int (input ("Input qauntity of Watermelon\n"));
for i in range (q_watermelon):
    melon_weight = int (input (f"Input weigt of Melon {i + 1}\n"));
    if i == 0:
        max = min = melon_weight;
    elif melon_weight > max:
            max = melon_weight;
    elif melon_weight < min:
            min = melon_weight;
print (f"The lightest melon is {min}kg, The graitest melon is {max}kg");
    
    
