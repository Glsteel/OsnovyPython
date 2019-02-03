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
# def max_string(*words):
#     list_of_lenght = []
#     for word in words:
#         lenght_of_word = len(word)
#     print(lenght_of_word)
#     #     list_of_lenght.append(lenght_of_word)
#     # longest_word = list_of_lenght.index(max(list_of_lenght))
#     # print(words[longest_word])
#
# megastring = ("строка", "составленная", "из", "других", "слов")
# max_string(megastring)


# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

import os
peoples = ['Иванов', 'Петров', 'Смирнов', 'Рокфеллер', 'Гейтс']
pays = [10000, 20000, 15000, 1000000, 550000]
pay_list = dict(zip(peoples, pays))
big_salary = []
for key, item in pay_list.items():
    if item >= 500000:
        big_salary.append(key)
for key in big_salary:
    del pay_list[key]
# print(pay_list)

salary = open('salary.txt', 'w', encoding='utf-8')
for people, pay in pay_list.items():
    salary.write(people+' - '+str(pay)+'\n')
salary.close()

with open('salary.txt', encoding='utf-8') as salary:
    for line in salary:
        zp = line.find('-') + 2
        a = float(line[zp:]) * 0.87
        # print(a)
        print(line[:zp - 1].upper(), a)


