"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort(reverse=True)
    max_1 = my_list[0]
    max_2 = my_list[1]
    return ("Сумма наибольших двух чисел >>> ", max_1 + max_2)


var_1 = int(input("Введите число №1 >>> "))
var_2 = int(input("Введите число №2 >>> "))
var_3 = int(input("Введите число №3 >>> "))
print(my_func(var_1, var_2, var_3))
