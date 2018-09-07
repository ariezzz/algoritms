# -*- encoding: utf-8 -*-
# 1. Пользователь вводит данные о количестве предприятий,
#  их наименования и прибыль за 4 квартала для каждого
#  предприятия. Программа должна определить среднюю
#  прибыль (за год для всех предприятий) и вывести
#  наименования предприятий, чья прибыль выше среднего
#  и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

# Примечание: 4 квартала - это 4 разных прибыли ;-)
from collections import defaultdict


q_naim = int(input('Введите количество предприятий: \t'))

d = defaultdict(float)

for _ in range(q_naim):

    naim = input('Введите название организации:\t')

    for i in range(4):

        profit = float(input(f'Введите прибыль {naim} за {i + 1} квартал:\t'))

        d[naim] += profit

avg = sum(d.values()) / len(d)

min_profit = [i for i, j in d.items() if j < avg]

max_profit = [i for i, j in d.items() if j > avg]

print(f'Средняя прибыль {avg}')

print(f'Предприятия с выручкой ниже среднего {min_profit}')

print(f'Предприятия с выручкой выше среднего {max_profit}')
