# -*- encoding: utf-8 -*-
# 1. Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы.
# Результаты анализа вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.

# Python 3.6.5
# Ubuntu x86_64

import sys
import random


def get_size(x, summ=0):

    if hasattr(x, '__iter__'):

        if hasattr(x, 'items'):

            for y in x.items():

                summ = get_size(y, summ)

        elif not isinstance(x, str):

            for y in x:

                summ = get_size(y, summ)

    summ += sys.getsizeof(x)

    return summ


# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).
# summ = 0

def task1():

    number = int(input('введите натуральное число:\t'))

    even = odd = 0

    while number > 0:

        if number % 2 == 0:

            even += 1

        else:

            odd += 1

        number = number // 10

    print(f"четных - {even}, нечетных - {odd}")

    return locals().values()


summ = 0

for i in task1():

    summ += get_size(i)

print(f'Все переменные первой задачи занимают = {summ} байт')


# 3. В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.


def task2():
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

    return locals().values()


summ = 0

for i in task2():

    summ += get_size(i)

print(f'Все переменные второй задачи занимают = {summ} байт')


# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена.

def eratocfen(number):

    if number > 9593:

        print('Эта программа может посчитать только 9592 чисел')

        return

    n = 100000

    sieve = [i for i in range(n)]

    sieve[1] = 0

    for i in range(2, n):

        if sieve[i] != 0:
            j = i * 2

            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]

    print(res[number - 1])

    return locals().values()


summ = 0

for i in eratocfen(9592):

    summ += get_size(i)

print(f'Все переменные третьей задачи занимают = {summ} байт')
