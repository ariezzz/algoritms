# 8. Определить, является ли год, который ввел пользователем,
# високосным или невисокосным.

year = int(input('Введите год'))

if year % 4 != 0:

    print('Год не является високосным')

elif year % 400 == 0:

    print('Год не является високосным')

else:

    print('Год является високосным')