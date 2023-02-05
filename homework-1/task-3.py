# 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

firstX = int(input("Введите координату первого X "))
firstY = int(input("Введите координату первого Y "))
secondX = int(input("Введите координату второго X "))
secondY = int(input("Введите координату второго Y "))

tempX = pow(secondX - firstX, 2)
tempY = pow(secondY - firstY, 2)

result = math.sqrt(tempX + tempY)

print(f"Расстояние между двумя точками {round(result,2)}")
