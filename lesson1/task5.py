# 5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

start = input('введите первую букву ')

stop = input('введите вторую букву ')

ord_start = ord(start)

ord_stop = ord(stop)

place_start = ord_start - 96

place_stop = ord_stop - 96

result = abs(ord_start - ord_stop)

print(f'''буква {start} находится на {place_start} месте,
буква {stop} находится на {place_stop} месте,
между ними {result} букв''')