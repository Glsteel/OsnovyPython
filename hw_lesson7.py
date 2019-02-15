# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# 	Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 	Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 	Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 11     - 14    87
#       16 49    55 77    88
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)

import random

class Card:
    def __init__(self, player_name):
        self.player_name = player_name
        self.card_numbers = []

    def create_card(self):
        # self.card_numbers = []
        while len(self.card_numbers) < 15:
            number = str(random.randint(1, 90))
            if number not in self.card_numbers:
                self.card_numbers.append(number)
        card_numbers_line1 = list(self.card_numbers[0:5])+list(' ' * 4)
        random.shuffle(card_numbers_line1)
        card_numbers_line2 = list(self.card_numbers[5:10]) + list(' ' * 4)
        random.shuffle(card_numbers_line2)
        card_numbers_line3 = list(self.card_numbers[10:]) + list(' ' * 4)
        random.shuffle(card_numbers_line3) # понятно, что это можно как-то укоротить, но сходу не придумал, а времени нет
        # print(card_numbers)
        # print(card_numbers_line1)
        # print(card_numbers_line2)
        # print(card_numbers_line3)
        self.card_numbers = card_numbers_line1 + card_numbers_line2 + card_numbers_line3
        return self.card_numbers

    def print_card(self):
        print('\n{}s card'.format(self.player_name)) # не нашел как отобразить в строке сам знак '
        print('-' * 50)
        print(self.card_numbers[0:9])
        print(self.card_numbers[9:18])
        print(self.card_numbers[18:])
        print('-' * 50)

print('\nДобро пожаловать в игру ЛОТО\n')
player_name = input('Enter player name: ', )

player_card = Card(player_name)
computer_card = Card('Computer')

player_card.create_card()
player_card.print_card()
computer_card.create_card()
computer_card.print_card()
# while True:
barrel_list = list(range(1, 91))
current_barrel = random.randint(0, len(barrel_list))
print(barrel_list)
print(current_barrel)

    # barrel_list.append(current_barrel)
    # print('Выпал бочонок номер: ', current_barrel)
    # for current_barrel in barrel_list:
    #     if current_barrel not in barrel_list:
    #         barrel_list.append(current_barrel)
    #         print('Выпал бочонок номер: ', current_barrel)

