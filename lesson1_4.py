# 1.4[8]. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Примеры/Тесты:
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите ширину шоколадки:>> "))
m = int(input("Введите длинну шоколадки:>> "))
k = int(input("Введите количество долек которое вы хотите отломить:>> "))

if k-1 > n*m-1:
    print("no")
else:
    can_break = False
    for i in range(1, n):
        if k % i == 0 and k//i <= m:
            can_break = True
            break
    for j in range(1, m):
        if k % j == 0 and k//j <= n:
            can_break = True
            break
    if can_break:
        print("yes")
    else:
        print("no")