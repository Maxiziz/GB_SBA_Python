# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds_inp = int(input('Введите количество секунд >>>'))
a = seconds_inp // 60
hours = a // 60
minutes = a % 60
seconds = seconds_inp % 60

print('{}:{}:{}'.format(hours, minutes, seconds))