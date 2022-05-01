# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Решение через dict

m = int(input("Введите номер месяца в виде числа от 1 до 12 >>>"))
seasons_dict = {1: "зиме", 2: "зиме", 3: "весне", 4: "весне", 5: "весне", 6: "лету",
                7: "лету", 8: "лету", 9: "осени", 10: "осени", 11: "осени", 12: "зиме"}

if m > 12 or m < 1:
    print ("Введено некорректное число. Число должно быть от 1 до 12.")
    exit(0)

print(f"{m}-й месяц года относится к {seasons_dict.get(m)}.")