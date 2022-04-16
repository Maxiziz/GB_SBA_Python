# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

Revenue = int(input('Введите значение выручки($) >>>'))
Costs =  int(input('Введите значение издержек($) >>>'))
Fin_result = Revenue - Costs

if Fin_result > 0:
    print('Финансовый результат положительный. Компания прибыльна. Прибыль составила:', Fin_result, '$')
    print('Рентабельность выручки составила:', int((Fin_result / Revenue) * 100), '%')
    Emp_nmb = int(input('Теперь введите численность сотрудников >>>'))
    print('Прибыль фирмы в расчете на одного сотрудника составила:', int(Fin_result / Emp_nmb), '$')
elif Fin_result == 0:
    print ('Финансовый результат нулевой. Компания находится в точке безубыточности.')
else:
    print('Финансовый результат отрицательный. Компания убыточна. Убыток составил:', Fin_result, '$')