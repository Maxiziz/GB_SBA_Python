# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

s = input("Введите строку из нескольких слов, разделенных пробелами >>>")
lst = s.split()
q = 0

for el in lst:
    if len(el) > 10:
        print(el[0:10])
        q = 1
    else:
        print(el)

if q == 1:
    print("* слова длинне 10 букв были ограничены 10 символами")