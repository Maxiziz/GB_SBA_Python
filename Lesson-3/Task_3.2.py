"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(firstname, lastname, birthyear, currentcity, email, phonenumber):
    print(
        "Имя: ", firstname,
        "; Фамилия: ", lastname,
        "; Год рождения: ", birthyear,
        "; Город проживания: ", currentcity,
        "; Email: ", email,
        "; Телефон: ", phonenumber,
    )


user_data(
    email="ivanovivan@maail.ru",
    phonenumber="+7(999) 999-99-99",
    birthyear=2525,
    currentcity="Иваново",
    firstname="Иван",
    lastname="Иванов"
)

# print и так выводит в одну строку.. в чем смысл этой оговорки в задании?
# можно было бы и f-строку одну сделать также..
# Можно было бы сделать несколько print в функции с end=''
# Или чтобы функция "оборачивала" данные, приписывая им словестное описание, выдавала бы результат в виде кортежа,
# а его уже через цикл выводить с принтов с end=''
# Видимо, проблема в том, что задание слишком "плоское": принять и вывести..