# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

products = []
n = 1
atribute_keys = ['Название', 'Цена(руб.)']

while True:
    y = input("Введите `Y`, если хотите добавить товар, или введите `N`, если хотите просмотреть аналитику >>>")
    while y != "Y" and y != "N":
        print("Введен неверный символ!")
        y = input("Введите Y, если хотите добавить товар, или введите N, если хотите просмотреть аналитику >>>")
    if y == "Y":
        print(f"Добавление товара №{n}. "
              f"Сначала, Вам будет предложено заполнить уже существующие в базе атрибуты, "
              f"после чего Вы сможете добавить новые атрибуты в систему.")
        vsego_atributov = len(atribute_keys)
        atributes = {}
        i = 0
        while i < vsego_atributov:
            atribut_key = atribute_keys[i]
            atribut_value = input(f"Введите `{atribut_key}` для товара {n}: ")
            atributes[atribut_key] = atribut_value
            i += 1
        while True:
            x = input(f"Введите `Y`, если хотите добавить новый атрибут в систему, или введите `N`, если хотите завершить добавление товара {n} >>>")
            while x != "Y" and x != "N":
                print("Введен неверный символ!")
                x = input(f"Введите `Y`, если хотите добавить новый атрибут в систему, или введите `N`, если хотите завершить добавление товара {n} >>>")
            if x == "Y":
                atribute_key = input("Введите название атрибута: ")
                atribute_value = input(f"Введите `{atribute_key}` для товара {n}: ")
                atributes[atribute_key] = atribute_value
                atribute_keys.append(atribute_key)
            elif x == "N":
                break
        products.append(tuple([n, atributes]))
        n += 1
    elif y == "N":
        break

analytics = {}
for product in products:
    for atribute_key, atribute_value in product[1].items():
        if atribute_key in analytics:
            analytics[atribute_key].append(atribute_value)
        else:
            analytics[atribute_key] = [atribute_value]

print(analytics)
print("Список характеристик и их значений:")
for a_key, a_value in analytics.items():
    print(a_key, ":", a_value)
