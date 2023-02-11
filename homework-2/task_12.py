''' Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.

Пример: 
4 4 -> 2 2
5 6 -> 2 3 '''

import random

x = random.randrange(1000)
y = random.randrange(1000)

print(f"Задуманное число X: {x}, задуманное число Y: {y}")

def getHints(x, y):

    s = x + y 
    p = x * y

    return s, p

def getTheHiddenNumbers(s, p):

    i = 1
    while i <= s:
        n = s - i
        if n * i == p:
            return i, n

        i += 1

s, p = getHints(x, y)
result1, result2 = getTheHiddenNumbers(s, p)
print(f"Подсказка: сумма чисел = {s}, произведение чисел = {p}")
print(f"Ответ: число X = {result1}, число Y = {result2}")