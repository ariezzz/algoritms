# 4. Определить, какое число в массиве встречается чаще всего.

import random

random_list = [random.randint(0, 100) for i in range(0, 10)]

max_el = 1
element = random_list[0]

for i in range(len(random_list)):

    el = 1

    for j in range(i, len(random_list)):

        if random_list[i] == random_list[j]:

            el += 1

    if el > max_el:

        max_el = el

        element = random_list[i]

print(f'{element} встречается {max_el} раз'
      if max_el > 1 else 'элементы не повторяются')
