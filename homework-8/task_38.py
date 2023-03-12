def displayListOfContacts():
    with open("homework-8/telephoneDirectory.txt", "r") as file:
        print(f"Список контактов: \n{file.read()}")

def addContact(data):
    with open("homework-8/telephoneDirectory.txt", "a") as file:
        file.write(f"\n{data}")
        print("Контакт добавлен.")

def searchContact(data):
    with open("homework-8/telephoneDirectory.txt", "r") as file:
        for line in file:
            if data in line:
                print(line)
                return line

def changingContact(data):
    contact = searchContact(data)
    new_name = input("Введите новые данные(ФИО + номер): ")
    with open("homework-8/telephoneDirectory.txt", "r") as file:
        old_data = file.read()
    new_data = old_data.replace(contact, new_name + "\n")
    with open('homework-8/telephoneDirectory.txt', 'w') as file:
        file.write(new_data)
    print("Контакт изменен.")

def deleteContact(data):
    contact = searchContact(data)
    with open("homework-8/telephoneDirectory.txt", "r") as f:
        lines = f.readlines()
    with open("homework-8/telephoneDirectory.txt", "w") as f:
        for line in lines:
            if line != contact:
                f.write(line)
    print("Контакт удален.")

# Изменение и удаление через replace()
# def modifyThePhoneDirectory(data, m):
#     contact = searchContact(data)
#     with open("homework-8/telephoneDirectory.txt", "r") as file:
#         old_data = file.read()
#     new_data = old_data.replace(contact, m)
#     with open('homework-8/telephoneDirectory.txt', 'w') as file:
#         file.write(new_data)

# def changingContact(data):
#     new_name = input("Введите новые данные(ФИО + номер): ")
#     modifyThePhoneDirectory(data, new_name + "\n")
#     print("Контакт изменен.")

# def deleteContact(data):
#     modifyThePhoneDirectory(data, '')
#     print("Контакт удален.")

value = int(input("Введите 1, чтобы вывести весь список контактов \
                  \nВведите 2, чтобы добавить новый контакт \
                  \nВведите 3, для поиска контакта \
                  \nВведите 4, для изменения контакта \
                  \nВведите 5, для удаления контакта\n"))

if value == 1: displayListOfContacts()
elif value == 2: addContact(input("Введите ФИО + номер телефона: "))
elif value == 3: searchContact(input("Введите имя или фамилию для поиска: "))
elif value == 4: changingContact(input("Введите имя и фамилию контакта который хотите изменить: "))
elif value == 5: deleteContact(input("Введите имя и фамилию контакта который хотите удалить: "))
