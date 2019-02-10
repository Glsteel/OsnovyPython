# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, brand, model, color, max_speed, is_police):
        self.brand = brand
        self.model = model
        self.color = color
        self.max_speed = int(max_speed) if int(max_speed) >= 0 else 0
        self._is_police = bool(is_police)

    def go(self):
        print('Поехали')

    def stop(self):
        print('Стоп')

    def turn(self, direction): #По-русски или по-английски передаем функции данные о направлении движения.
        if direction.find('лев') >= 0 or direction.find('left') >= 0:
            print('Поворачиваем налево')
        elif direction.find('прав') >= 0 or direction.find('right') >= 0:
            print('Поворачиваем направо')
        else:
            print('Определись с маршрутом!')

class Taxi(Car):
    def __init__(self, brand, model, color, max_speed, is_police, num_of_passengers):
        Car.__init__(self, brand, model, color, max_speed, is_police)
        self.num_of_passengers = int(num_of_passengers)

    def charge(self, charge):
        print('Стоимость составит: {} руб.'.format(charge))


class SportCar(Car):
    def __init__(self, brand, model, color, max_speed, is_police, quantity_of_no3):
        Car.__init__(self, brand, model, color, max_speed, is_police)
        self.quantity_of_no3 = float(quantity_of_no3)


car1 = Car('Ford', 'Focus', 'black', 150, False)
print('Максимальная скорость: {}'.format(car1.max_speed))
car1.go()
direction = input('Впереди перекресток, введите направление движения: ', )
car1.turn(direction)
car1.stop()

car2 = Taxi('Nissan', 'Sentra', 'white', 120, 0, 4)
print(car2._is_police)



