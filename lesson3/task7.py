# 7. В одномерном массиве целых чисел определить два наименьших
# элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

import random


random_list = [random.randint(0, 100) for i in range(0, 10)]


min1 = random_list[0]

min2 = random_list[1]

if min1 > min2:

    min1, min2 = min2, min1

for i in random_list:

    if i < min1:

        b = min1

        min1 = i

        if b < min2:

            min2 = b

    elif i < min2:

        min2 = i

print(random_list)

print(min1, min2)
