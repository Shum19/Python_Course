# Задача 2
# Петя и Катя – брат и сестра. Петя – студент, а Катя –школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных
# числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя
# делает две подсказки. Он называет сумму этих чисел S и их 
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3
summary = int(input("Input a summary - "));
product = int(input ("Input a product - "));
for y in range (1, product + 1):
    if product % y == 0:
        x = product // y
        if x + y == summary:
            print (y, x);
            break;
else: 
    print ("Somthing went wrong!")