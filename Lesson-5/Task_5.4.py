"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

vocabulary = {"One": "Odin", "Two": "Dva", "Three": "Tri", "Four": "Chetire"}
content = []

with open("file4_1.txt") as my_file:
    for line in my_file:
        words_list = line.split(" - ")
        if words_list[0] in vocabulary:
            word = vocabulary[words_list[0]]
            content.append(word + " - " + words_list[1])

with open("file4_2.txt", "w") as new_file:
    new_file.writelines(content)
