# Задача 1
# Найдите сумму цифр трехзначного числа.
# in 123 out 6
digit = int(input("Input digit\n"));
summary = 0;
while digit > 0:
    digitSeparate = digit % 10;
    summary += digitSeparate;
    digit = digit // 10;
print (summary);