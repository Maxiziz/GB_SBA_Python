# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

new_list=[]
result_list=[]
a = None
while a != "stop":
    a = input("Введите элемент списка или введите `stop` для просмотра результата >>>")
    if a != "stop":
        new_list.append(a)

print(new_list)

b = len(new_list)
i = 0
if b < 2:
    print("Введите как минимум два элемента списка!")
    b=0
while i + 1 <= b:
    if i + 1 == b:
        result_list.append(new_list[i])
    else:
        result_list.extend([new_list[i+1], new_list[i]])
    i += 2

print(result_list)