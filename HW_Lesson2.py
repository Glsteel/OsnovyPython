# Домашнее задание, урок 2
# Сложность: Easy

# Задача 1
fruits = ['apple', 'orange', 'grapefuit', 'peach']
count = 1
for fruit in fruits:
    print(str(count)+'.'+'{:>10}'.format(fruit))
    count = count + 1
print()
print()

# Задача 2
massive_1 = [1, 2, 2, 3, 5, 7.5, 9.75, 'один']
print('Первый список: ', massive_1)
massive_2 = [1, 2, 4, 6, 8, 9.75, 'один']
print('Второй список: ', massive_2)
mass_sovp = []
mass_sovp_count = []
count = 0
for el_1 in massive_1:
    for el_2 in massive_2:
        if el_1 == el_2:
            mass_sovp.append(el_1)
            mass_sovp_count.append(count)
    count = count + 1
print("Совпадающие элементы", mass_sovp, " удаляем их из первого списка")
while len(mass_sovp_count) > 0:
    del_el = mass_sovp_count.pop()
    massive_1.pop(del_el)
print('Теперь первый список выглядит так: ', massive_1)
print()
print()

#Задача 3
massive_3 = [1, 2, 5, 8, 22, 4, 58, 33, 17]
target_massive = []
for i in massive_3:
    if i % 2 == 0:
        target_massive.append(i / 4)
    else:
        target_massive.append(i * 2)
print(target_massive)

