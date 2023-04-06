# Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. Пользователь вводит это число с клавиатуры, список можно считать заданным. Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10

lst = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
x = int(input("Введите число: "))

closest = lst[0]  # предполагаем, что ближайший элемент - это первый элемент списка

for num in lst:
    if abs(num - x) < abs(closest - x):
        closest = num

print(closest)
