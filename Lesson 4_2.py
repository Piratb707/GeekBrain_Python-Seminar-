# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом. На входе задано количество ягод на каждом кусте. Не обязательно вводить их с клавиатуры, можно задать непосредственно в коде программы
#
# Примеры/Тесты:
# Input1: 1, 2, 3, 4, 5, 6, 7, 8
# Output1: Макс. кол-во ягод 21, собрано для куста 7
#
# Input1: 11, 92, 1, 42, 15, 12, 11, 81
# Output1: Макс. кол-во ягод 184, собрано для куста 1


berries = [1, 2, 3, 4, 5, 6, 7, 8]  # ягоды на кустах
n = len(berries)  # количество кустов

max_berries = 0  # максимальное количество ягод
max_bush = 0  # номер куста с максимальным количеством ягод

for i in range(n):
    # вычисляем номера двух соседних кустов
    left = (i - 1 + n) % n
    right = (i + 1) % n

    # вычисляем количество ягод, которое может собрать модуль
    sum_berries = berries[i] + berries[left] + berries[right]

    # обновляем максимальное количество ягод и номер куста
    if sum_berries > max_berries:
        max_berries = sum_berries
        max_bush = i + 1

if max_berries == 0:
    print("На грядке нет ягод")
else:
    print("Максимальное количество ягод", max_berries, "собрано для куста", max_bush)

