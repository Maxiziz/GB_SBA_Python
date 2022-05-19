"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

import sys

try:  # Скрипт необходимо запускать с тремя параметрами.
    file, work_hours, hourly_rate, bonus = sys.argv
except ValueError:
    print("Invalid parameters")
    exit()


def salary_calculate(work_hours, hourly_rate, bonus):
    salary = (round(float(work_hours) * float(hourly_rate), 2) + float(bonus))
    return salary


print(salary_calculate(work_hours, hourly_rate, bonus))
