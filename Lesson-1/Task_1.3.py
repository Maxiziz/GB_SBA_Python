# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = int(input('Введите число >>>'))
nn = n * 10 + n
nnn = n * 100 + n * 10 + n
total = n + nn + nnn

print('{}+{}+{}={}'.format(n, nn, nnn, total))