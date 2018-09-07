# -*- encoding: utf-8 -*-
# 2. Написать программу сложения и умножения двух
# шестнадцатеричных чисел. При этом каждое число
# представляется как массив, элементы которого это цифры числа.

# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import OrderedDict, deque


def hex_to_ten(hex_n):

    hex_number = OrderedDict()

    for key, value in enumerate(NUMBERS):

        hex_number[value] = key

    return sum([hex_number[j] * (16**i) for i, j in enumerate(hex_1)])


def ten_to_hex(int_n):

    int_number = OrderedDict()

    for key, value in enumerate(NUMBERS):

        int_number[key] = value

    lst = []

    while int_n > 0:

        lst.append(int_n % 16)

        int_n = int_n // 16

    return [int_number[i] for i in lst[::-1]]



NUMBERS = '0123456789abcdef'


hex_1 = deque(input('Введите первое число\t'))

hex_1.reverse()

hex_2 = deque(input('Введите второе число\t'))

hex_2.reverse()

int_1 = hex_to_ten(hex_1)

int_2 = hex_to_ten(hex_2)


sum_ = ten_to_hex(int_1 + int_2)

mull_ = ten_to_hex(int_1 * int_2)

print(f'Сумма чисел\t{sum_}')
print(f'произведение чисел\t{mull_}')
