# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = []

for i in range(5):

    sub_matrix = []

    for j in range(10):

        number = random.randint(0, 100)

        sub_matrix.append(number)

    matrix.append(sub_matrix)

min_el = list()

for lst in matrix:

    element = float('inf')

    for i in lst:

        if element > i:

            element = i

    min_el.append(element)

element = 0

for i in min_el:

    if i > element:

        element = i

for i in matrix:

    print(i)

print(element)