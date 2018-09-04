# -*- encoding: utf-8 -*-
# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена. Второй - без
# использования "решета". Проанализировать скорость и сложность алгоритмов.
import timeit
import cProfile


def eratocfen(number):

    if number > 9593:

        # не смог придуматься как сделать без этого ограничения

        print('Эта программа может посчитать только 9592 чисел')

        return

    n = 100000

    sieve = [i for i in range(n)]

    sieve[1] = 0

    for i in range(2, n):

        if sieve[i] != 0:
            j = i * 2   # j = i + i

            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]

    return res[number - 1]



# cProfile.run('eratocfen(9592)')
# 1    0.038    0.038    0.047    0.047 task2.py:7(eratocfen)
# python -m timeit -s "import task2" "task2.eratocfen(1000)"
# 10 loops, best of 3: 62.5 msec per loop

def iter():

    i = 1

    while True:

        i += 1

        yield i


def easy(n):

    lst = []

    for i in iter():

        for j in range(2, i):

            if i % j == 0:

                break
        else:

            lst.append(i)

        if len(set(lst)) == n:

            return lst[-1]

# cProfile.run('easy(1000)')
# 1    0.472    0.472    0.474    0.474 task2.py:53(easy)
# cProfile.run('easy(2000)')
# 1    2.270    2.270    2.277    2.277 task2.py:53(easy)
# python -m timeit -s "import task2" "task2.easy(100)"
# 100 loops, best of 3: 3.93 msec per loop
# python -m timeit -s "import task2" "task2.easy(300)"
# 10 loops, best of 3: 52.9 msec per loop