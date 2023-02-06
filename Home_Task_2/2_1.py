# Задача 1 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество
# монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
# 2
import os;
os.system('clear')

coins_quantity = int (input("Input quantity of Coins - "))
eagle_side = tail_side = 0;
print("Now you're going to input sides of coins!"
      "\nEagle Side is 1\nTail Side is 0")
for i in range(coins_quantity):
    sides = int (input (f"Coin number {i+1} - "))
    if sides == 1:
        eagle_side += 1;
    else:
        tail_side +=1;
if tail_side < eagle_side:
    print (f"You need to turn {tail_side} coins");
else:
    print (f"You need to turn {eagle_side} coins");