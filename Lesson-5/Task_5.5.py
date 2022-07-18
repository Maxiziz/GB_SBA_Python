"""
5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint

line = [randint(1, 100) for i in range(5)]

with open("file5.txt", "w") as my_file:
    my_file.write(" ".join(map(str, line)))

with open("file5.txt") as my_file:
    content = my_file.read().split()
    numbers = [int(x) for x in content]
    print(sum(numbers))
