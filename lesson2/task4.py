# 4. Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

quantity = int(input('введите количество элементов:\t'))

element = 1

summ = 0

for i in range(quantity):

    summ += element

    element /= -2

print(f'сумма равна: {summ}')
