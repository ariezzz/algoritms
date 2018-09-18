#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 1. Отсортировать по убыванию методом «пузырька»
# одномерный целочисленный массив, заданный случайными
# числами на промежутке [-100; 100). Вывести на экран
# исходный и отсортированный массивы.

from random import randint

lst = [randint(-100, 99) for _ in range(16)]


def sort_puz(lst):

    n = 1

    sorted_ = 0

    while n < len(lst):

        if sorted_ >= len(lst) - n:

            return lst

        for i in range(len(lst) - n):

            if lst[i] > lst[i + 1]:

                lst[i], lst[i + 1] = lst[i + 1], lst[i]

                sorted_ = 0

            else:

                sorted_ += 1

        n += 1

    return lst


if __name__ == '__main__':

    print(lst)
    print(sort_puz(lst[:]))
