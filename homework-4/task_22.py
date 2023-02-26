''' Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.nПользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.

Пример: 
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18

6 12 '''

from random import randint

def getList(number):
    random_list = [randint(1, 100) for _ in range(number)]
    print(random_list)
    return set(random_list)

listN = getList(int(input("Введите число N: ")))
listM = getList(int(input("Введите число M: ")))

number_list = listN.intersection(listM)

if number_list == set():
    print('нет совпадающих чисел')
else:
    print(f"Совпадающие числа в порядке возрастания: {sorted(number_list)}")