# 1.1[2]. Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод
# Например для числа 145 сумма цифр будет 10: 1 + 4 + 5
# Примеры/Тесты:
# 123 >>> Сумма чисел числа 123 равна 6
# 100 >>> Сумма чисел числа 100 равна 1
# (*) Усложнение. Решите для числа произвольной разрядности: произвольное количество цифр в числе.
# (**) Усложнение. Для числа произвольной разрядности добавить в вывод строку с числами, например так:
# 13579 >>> Сумма чисел числа 13579 равна 25(1 + 3 + 5 + 7 + 9)

# num = 767
# num = input("Введите число :>> ")
# sum_of_digits = int(num[0]) + int(num[1]) + int(num[2])
# print(f"Сумма цифр числа {num} равна: {sum_of_digits}")

# Усложнение 1 Решите для числа произвольной разрядности: произвольное количество цифр в числе.

# num = input("Введите число:>> ")
# digit_sum = 0
# for digit in num:
#     digit_sum += int(digit)
# print(f"Сумма цифр числа {num} равна: {digit_sum}")


# Усложнение 2 Для числа произвольной разрядности добавить в вывод строку с числами.

# num = input("Введите число:>> ")
# digit_sum = 0
# digits = []
# for digit in num:
#     digit_sum += int(digit)
#     digits.append(digit)
# digit_str = " + ".join(digits)
# print(f"Сумма цифр числа {num} равна: {digit_sum} ({digit_str})")

