''' Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
Пример: 10 -> 1 2 4 8 '''

numberN = int(input("Задайте число N: "))

for i in range(numberN):
    n = 2**i
    if n < numberN:
        print(n)
    elif n > numberN:
        break
