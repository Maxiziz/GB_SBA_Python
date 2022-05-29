"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

Пример файла:
Иванов 23543.12
Петров 13749.32
"""

from statistics import mean

with open("file3.txt") as my_file:
    content = my_file.readlines()
    salarys = []
    print("Список сотрудников с окладом менее 20 тыс.:")
    for line in content:
        words_list = line.split()
        salarys.append(float(words_list[1]))
        if float(words_list[1]) < 20000:
            print(line.replace('\n', ''))
    print("\nСредняя величина оклада среди всех сотрудников:", round(mean(salarys), 2))
