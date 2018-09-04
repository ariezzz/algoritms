# -*- encoding: utf-8 -*-
# 1. Проанализировать скорость и сложность одного-трёх любых
# алгоритмов, разработанных в рамках домашнего задания первых трех уроков.

import timeit
import cProfile
import random

def change(num):

    random_list = [random.randint(-100, 100) for i in range(0, num)]


    max_el = -float('Inf')

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

    return random_list


# cProfile.run('change(1000)')
# 1    0.000    0.000    0.003    0.003 task1.py:8(change)
# cProfile.run('change(10000)')
# 1    0.001    0.001    0.036    0.036 task1.py:8(change)
# cProfile.run('change(100000)')
# 1    0.016    0.016    0.486    0.486 task1.py:8(change)

# python -m timeit -s "import task1" "task1.change(1000)"
# 100 loops, best of 3: 2.08 msec per loop