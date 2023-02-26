''' Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.

Пример: 
4 -> 1 2 3 4
9 '''

from random import randint

numberOfBushes = int(input("Введите количество кустов черники: "))

numberOfBerries = [randint(1, 100) for _ in range(numberOfBushes)]
print(numberOfBerries)

listOfAmounts = []

for index in range(len(numberOfBerries)):

    if index < len(numberOfBerries) - 1:
        numberOnTheLeft = numberOfBerries[index - 1]
        numberOnTheRight = numberOfBerries[index + 1]
    else:
        numberOnTheLeft = numberOfBerries[index - 1]
        numberOnTheRight = numberOfBerries[0]

    sumOfBerries = numberOfBerries[index] + numberOnTheLeft + numberOnTheRight
    listOfAmounts.append(sumOfBerries)

print(listOfAmounts)
print(f"Максимальное количество ягод способный собрать собирающий модуль за один заход: {max(listOfAmounts)}")
