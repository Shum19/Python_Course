# Задача 1
# За день машина проезжает n километров. Сколько дней нужно, 
# чтобы проехать маршрут длиной m километров? При решении этой 
# задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700 m = 750 Output: 2


n = int(input("Input Distance per Day:\n"));
m = int(input("Input Distance:\n"));
result = -(-m // n);
print (result);