# 7. Написать программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n – любое натуральное число.


elements = int(input('введите количество элементов:\t'))

summ = 0

for i in range(1, elements + 1):

    summ += i

function = elements * (elements + 1) / 2

if function == summ:

    print('равенство верно')

else:

    print('равенство не верно')

