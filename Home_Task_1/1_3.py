# Задача 3. 
# Вы пользуетесь общественным транспортом? Вероятно, 
# вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным
# номером, где сумма первых трех цифр равна сумме последних
# трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# in 385916 out yes
# in 123456 out no

# Method 1
ticketNumber = int(input("Input only 6th digit ticket number\n"))
leftPart = ticketNumber // 1000;
rightPart = ticketNumber % 1000;
sumOfLeftPart = 0;
sumOfRightPart = 0;
while leftPart > 0:
    leftDigit = leftPart % 10;
    rightDigit = rightPart % 10;
    sumOfLeftPart += leftDigit;
    sumOfRightPart += rightDigit;
    rightPart = rightPart //10;
    leftPart = leftPart // 10;
if sumOfLeftPart == sumOfRightPart:
    print("Today you are very lucky!!!");
else:
    print ("Sorry!Try next day to get lucky ticket!")

# Method 2
ticketNumber = input("Input ticket number\n")
leftPart = len(ticketNumber) // 2;
rightPart = len(ticketNumber) - leftPart;
sumOfLeftPart = 0;
sumOfRightPart = 0;
if len(ticketNumber) % 2 == 0: 
    for i in range(leftPart):
        sumOfLeftPart += int(ticketNumber[i]);
        sumOfRightPart += int(ticketNumber[rightPart])
        rightPart +=1;         
    if sumOfLeftPart == sumOfRightPart:
        print("Today you are very lucky!!!");
    else:
        print ("Sorry!Try next day to get lucky ticket!")
else:
    print("Ticket number must have enen digits "
          "in its number")