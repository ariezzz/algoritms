# 3. Массив размером 2m + 1, где m – натуральное число,
# заполнен случайным образом. Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две
# равные части: в одной находятся элементы, которые не
# меньше медианы, в другой – не больше ее.

# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки,
# который не рассматривался на уроках.

from random import randint

m = int(input('Введите целое натуральное цисло:\t'))

array = [randint(-100, 100) for _ in range(2 * m + 1)]

array = [-19, 10, 17, 21, 21, 22, 31, 67, 73]

print(f'Список - {array}')

min_1 = float('Inf')

for i in array:

    if i < min_1:

        min_1 = i

counter = 0

min_2 = float('Inf')

while counter < m:

    for i in array:

        if min_1 < i <= min_2:

            min_2 = i

    min_1 = min_2

    min_2 = float('Inf')

    counter += 1

print(f'Медиана = {min_1}')

