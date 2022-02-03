"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула на право'

    def turn_left(self):
        return f'{self.name} повернула на лево'

    def show_speed(self):
        return f'Текущая скорость {self.name} составляет: {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость town car {self.name} составляет: {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышает разрешенную'
        else:
            return f'Скорость {self.name} не превышает разрешенную'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} состовляет: {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышает разрешенную'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} это полицейская машина'
        else:
            return f'{self.name} это не полицейская машина'


bmw = SportCar(100, 'Blak', 'BMW', False)
kia = TownCar(40, 'White', 'KIA', False)
reno = WorkCar(60, 'Orange', 'Reno', True)
ford = PoliceCar(110, 'Blue', 'Ford', True)
print(kia.turn_left())
print(f'Когда {reno.turn_right()}, то {bmw.stop()}')
print(f'{kia.go()} с разрешенной скоростью')
print(f'{bmw.name} это полицейская машина? {bmw.is_police}')
print(bmw.show_speed())
print(reno.show_speed())
print(ford.police())
print(ford.show_speed())
