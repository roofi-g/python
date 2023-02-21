''' Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. 
Последняя строка содержит число X

Пример: 
5
1 2 3 4 5
6
-> 5 '''

from random import randint

random_list = [randint(1, 100) for _ in range(10)]
print(random_list)

number_n = int(input("Введите число N от 0 до 100: "))

element = random_list[0]
currentDifference = abs(number_n - element)

for elem in random_list:
    difference = abs(elem - number_n)
    if difference < currentDifference:
        element = elem
        currentDifference = difference

print(element)


# Второй вариант решения. Работает только с положительными числами.

# minimumValue = max([n for n in random_list if n < number_n])
# maxValue = min([n for n in random_list if n > number_n])

# if number_n - minimumValue < maxValue - number_n:
#     print(minimumValue)
# else:
#     print(maxValue)
