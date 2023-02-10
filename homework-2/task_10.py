''' Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть. 

Пример: 
5 -> 1 0 1 1 0
2 '''

import random

numberOfCoins = int(input("Количество монеток: "))

def getRandomNumbers(numberOfCoins):
    coins = []
    
    for i in range(numberOfCoins):
        ran = random.random()
        coins.append(round(ran))
    
    return coins

def getTheMinAmount(coins):

    numberOfTails = coins.count(1)
    numberOfHeads = coins.count(0)

    if numberOfTails < numberOfHeads:
        return print(f"Минимальное количество монеток, которое нужно перевернуть: {numberOfTails}")
    else:
        return print(f"Минимальное количество монеток, которое нужно перевернуть: {numberOfHeads}")

coins = getRandomNumbers(numberOfCoins)
print(f"Список: {coins}")
getTheMinAmount(coins)
