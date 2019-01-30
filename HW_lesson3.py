# Основы Python. Домашнее задание 3
# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

# name = input("Введите имя: ", )
# age = input("Введите возраст: ", )
# city = input("Введите город проживания: ", )
# user = [name, age, city]
# def func_1(name, age, city):
#     print(name.title()+", "+age+" лет, проживает в городе "+city.title())
# func_1(name, age, city)

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
# def max_func(number_1, number_2, number_3):
#     max_number = max(number_1, number_2, number_3)
#     return max_number
# a = int(input("Введите число 1: "))
# b = int(input("Введите число 2: "))
# c = int(input("Введите число 3: "))
# print("Наибольшее из чисел: ", max_func(a, b, c))

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов
def max_string(*words):
    list_of_lenght = []
    for word in words:
        lenght_of_word = len(word)
    print(lenght_of_word)
    #     list_of_lenght.append(lenght_of_word)
    # longest_word = list_of_lenght.index(max(list_of_lenght))
    # print(words[longest_word])

megastring = ("строка", "составленная", "из", "других", "слов")
max_string(megastring)


