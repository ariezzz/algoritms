# 3. В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.

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

random_list[i_min], random_list[i_max] = random_list[i_max], random_list[i_min]

print(random_list)
