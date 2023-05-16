"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _length: int
    _width: int
    _rate = 25
    _thickness = 5

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def mass_calculate(self):
        mass = round(self._length * self._width * self._rate * self._thickness / 1000, 2)
        print(f"Масса асфальта = {mass} т.")

road = Road(5000, 20)
road.mass_calculate()
