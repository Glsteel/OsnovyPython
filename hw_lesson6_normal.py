# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

import random

class Unit:
    def __init__(self, max_health, health, damage, max_armor, armor):
        self._max_health = int(max_health)
        self.health = float(health)
        self.damage = tuple(damage) # подразумеваем, что это кортеж из двух целых чисел
        self._max_armor = int(max_armor)
        self.armor = float(armor)

    def _hit(self, damage, max_health, health): # возвращает величину урона зависящую от уровня здоровья
        health_level = health / (max_health / 100)
        if health_level >= 90:
            hit = max(damage)
        elif health_level <= 30:
            hit = min(damage)
        else:
            hit = (damage[0] + damage[1]) * (health_level / 100)
        return hit

    def attack(self, attacker, defender):
        # hit = _hit(attacker.damage)
        causing_gamage = defender.armor + defender.health - _hit(attacker.damage)
        causing_gamage = defender.a
        return causing_gamage


class Knight(Unit):
    def __init__(self, max_health, health, damage, max_armor, armor, repair):
        Unit.__init__(self, max_health, health, damage, max_armor, armor)
        self.repair = repair

    def repairing(self, repair, max_armor, armor):
        if repair - random.random() >= 0:
            rep_count = (max_armor - armor) * random.random()
        else:
            rep_count = 0
        return rep_count


class Healer(Unit):
    def __init__(self, max_health, health, damage, max_armor, armor, heal):
        Unit.__init__(self, max_health, health, damage, max_armor, armor)
        self.heal = heal

    def healing(self, heal, max_health, health):
        if heal - random.random() >= 0:
            heal_count = (max_health - health) * random.random()
        else:
            heal_count = 0
        return heal_count


# peasant1 = Unit(10, 7, (1, 3), 0, 0)
# peasant2 = Unit(12, 12, (2, 3), 0, 0)
# hit1 = peasant1._hit(peasant1.damage, peasant1._max_health, peasant1.health)
# print(hit1)

healer1 = Healer(20, 1, (5, 7), 5, 5, 0.5)
print(healer1.healing(healer1.heal, healer1._max_health, healer1.health))
