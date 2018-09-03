# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

random_list = [random.randint(-100, 100) for i in range(0, 10)]

max_el = 0

for i, j in enumerate(random_list):

    if j < max_el:

        max_el = j

        i_max = i


print(f'максимальное отрицательное число: {max_el} имеет {i_max} индекс')
