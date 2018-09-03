# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних
# элементов строк. Программа должна вычислять сумму введенных элементов
# каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

matrix = []

for i in range(4):

    sub_matrix = []

    summ = 0

    for j in range(4):

        number = int(input(f'Введите число в {j}-й столбец {i}-ую строку:\t'))

        summ += number

        sub_matrix.append(number)

    sub_matrix.append(summ)

    matrix.append(sub_matrix)

for i in matrix:

    print(i)
