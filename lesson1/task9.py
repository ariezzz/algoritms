# 9. Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите три числа: ')

a = int(input('a = '))

b = int(input('b = '))

c = int(input('c = '))

if b < a < c or c < a < b:

    print(f'Среднее: {a}')

elif a < b < c or c < b < a:

    print(f'Среднее: {b}')

else:

    print(f'Среднее: {c}')
