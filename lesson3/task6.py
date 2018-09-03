# 6. В одномерном массиве найти сумму элементов, находящихся
# между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

random_list = [random.randint(0, 100) for i in range(0, 10)]


max_el = 0

min_el = float('Inf')

print(random_list)

for i, j in enumerate(random_list):

    if j > max_el:

        max_el = j

        i_max = i

    if j < min_el:

        min_el = j

        i_min = i

summ = int()

if i_min > i_max:

    i_min, i_max = i_max, i_min

for i in random_list[i_min + 1:i_max]:

    summ += i

print(f'сумма равна {summ}')