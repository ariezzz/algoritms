#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N.
# Например, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом
# sha1 из модуля hashlib.


from hashlib import sha1


string = input('Введите строку: ')

sub_strings = set()

for i in range(len(string) + 1):

    for j in range(i + 1, len(string) + 1):

        sub = sha1(string[i:j].encode('utf-8')).hexdigest()

        sub_strings.add(sub)

print(f'подстрок = {len(sub_strings)}')
