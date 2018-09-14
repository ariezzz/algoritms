# 2. Отсортируйте по возрастанию методом слияния одномерный
# вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы

from random import randint

lst = [randint(0, 49) for _ in range(16)]


def merge(lst):

    leght = len(lst)

    if leght <= 1:

        return lst

    left = merge(lst[:leght // 2])
    right = merge(lst[leght // 2:leght])

    i = j = 0

    result = list()

    while i < len(left) or j < len(right):

        if not i < len(left):

            result.append(right[j])

            j += 1

        elif not j < len(right):

            result.append(left[i])

            i += 1

        elif left[i] < right[j]:

            result.append(left[i])

            i += 1

        else:

            result.append(right[j])

            j += 1

    return result


if __name__ == '__main__':

    print(lst)

    print(merge(lst[:]))
