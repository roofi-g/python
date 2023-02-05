# Задача 2: Найдите сумму цифр трехзначного числа. Пример: 123 -> 6 (1 + 2 + 3)

number = input("Введите трехзначное число: ")

def getSumDigits():
    
    sumDigits = 0

    for element in number:
        digit = int(element)
        sumDigits += digit
    
    return sumDigits

print(f"Сумма цифр в числе {number} равен: {getSumDigits()}")