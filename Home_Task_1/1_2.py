# Задача 2. 
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они 
# сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество 
# журавликов, а Катя сделала в два раза больше журавликов, чем Петя 
# и Сережа вместе?
# in 6 out 1 4 1
# in 24 out 4 16 4
# in 60 out 10 40 10
quantityOfGrus = int (input ("Input quantity of Grus\n"));
# Цифра 1 выполняет функцию переменной в уравнении
# petya = sergei = x
# katya = y
# y = 2 * (x + x)
# quantityOfGrus = y + x + x
# quantityOfGrus = 2 *(x + x) + x + x
# quantityOfGrus = 6x
# x = quantityOfGrus / 6
petyaX = 1;
sergeiX = petyaX;
katyaY = 2 * (petyaX + sergeiX);
petyaX = quantityOfGrus // (katyaY + sergeiX + petyaX);
sergeiX = petyaX;
katyaY = 2 * (petyaX + sergeiX);
if quantityOfGrus == katyaY + petyaX + sergeiX:
    print (f"{petyaX}, {katyaY}, {sergeiX}");
else:
    print ("wrong quantity")
