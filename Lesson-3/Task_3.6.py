"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Затем продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


# Странное задание, ведь есть функция str.title, результат выполнение которой соответствует и первой, и второй
# части задания. Её можно обернуть в свою функцию, но это не питонический подход.

# def int_func(word):
#     return word.title()

# Чтож, ладно, изобретем эту функцию заново.

def int_func(in_str):
    words_list = in_str.split()
    result = []
    for el in words_list:
        first_letter = el[:1].upper()
        word = first_letter + el[1:]
        result.append(word)
    return ' '.join(result)


print(int_func("some lower case string"))
