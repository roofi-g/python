''' Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

Пример: 
5 
1 2 3 4 5
3
-> 1 '''

from random import randint

random_list = [randint(1, 10) for _ in range(randint(1,20))]
print(random_list)

number_n = int(input("Введите число N от 0 до 10: "))

# amount = 0

# for elem in random_list:
#     if elem == number_n:
#         amount += 1

# print(amount)

print(random_list.count(number_n))