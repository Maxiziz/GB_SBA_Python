"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(
            self,
            name: str,
            surname: str,
            position: str,
            wage: int,
            bonus: int
    ):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.name} {self.surname}")

    def get_total_income(self):
        income = self._income.get("wage") + self._income.get("bonus")
        print(f"Доход с учётом премии: {income}")


test_data = [
    {
        'name': 'Ivan',
        'surname': 'Ivanov',
        'position': 'Scrum master',
        'wage': 40000,
        'bonus': 0
    },
    {
        'name': 'Petr',
        'surname': 'Petrov',
        'position': 'developer',
        'wage': 90000,
        'bonus': 60000
    },
    {
        'name': 'Irina',
        'surname': 'Ivanova',
        'position': 'service delivery manager',
        'wage': 60000,
        'bonus': 30000
    },
]

for el in test_data:
    position = Position(**el)
    position.get_full_name()
    position.get_total_income()
    print("___________________")
