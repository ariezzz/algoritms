# 9. Среди натуральных чисел, которые были введены, найти
# наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

max_sum = 0

max_number = 0

while True:

    number = int(input('введите натуральное число\n для выхода введите 0'))

    if number == 0:

        break

    m = number

    s = 0

    while number > 0:

        s += number % 10

        number //= 10

    if s > max_sum:

        max_sum = s

        max_number = m

print(f'Число {max_number}, имеет максимальную сумму цифр: {max_sum}')
