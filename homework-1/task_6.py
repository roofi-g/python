# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# Пример: 
# 385916 -> yes
# 123456 -> no

ticketNumber = str(385916)

firstHalf = ticketNumber[:3]
secondHalf = ticketNumber[3:]

def getSumElements(number):
    result = 0
    for element in number:
        result += int(element)
    return result

if getSumElements(firstHalf) == getSumElements(secondHalf):
    print("yes")
else:
    print("no")