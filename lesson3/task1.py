# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

a = dict()

for i in range(2, 10):

    a[i] = 0

for i in range(2, 100):

    for j in a.keys():

        if i % j == 0:

            a[j] = a[j] + 1

print(a)