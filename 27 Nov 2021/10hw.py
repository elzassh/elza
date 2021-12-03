#Вводится n чисел. Проверить, что среди них существует ровно два таких числа,
# что длина (количество цифр) каждого из них равна 3 или 5,
# а их цифры либо все четные, либо все нечетные.

n = int(input())
a = []
for i in range(n):
    num = int(input())
    a.append(num)

a1 = 0
a2 = 0
print(a)

tr = []
pt = []

for k in range(len(a)):
    if len(str(a[k])) == 3:
        tr.append(a[k])
    if len(str(a[k])) == 5:
        pt.append(a[k])


for k in range(len(tr)):
    if tr[k] % 2 == 0:
        if a1 != 0 and a2 != 0:
            a1 = 0
            a2 = 0
            break
        elif a1 != 0:
            a2 = tr[k]
        else:
            a1 = tr[k]
if a1 != 0 and a2 != 0:
    print(a1)
    print(a2)
    print("Есть 2 четных трехзначных числа")

for k in range(len(tr)):
    if tr[k] % 2 != 0:
        if a1 != 0 and a2 != 0:
            a1 = 0
            a2 = 0
            break
        elif a1 != 0:
            a2 = tr[k]
        else:
            a1 = tr[k]

if a1 != 0 and a2 != 0:
    print(a1)
    print(a2)
    print("Есть 2 нечетных трехзначных числа")


for k in range(len(pt)):
    if pt[k] % 2 == 0:
        if a1 != 0 and a2 != 0:
            a1 = 0
            a2 = 0
            break
        elif a1 != 0:
            a2 = pt[k]
        else:
            a1 = pt[k]
if a1 != 0 and a2 != 0:
    print(a1)
    print(a2)
    print("Есть 2 четных пятизначных числа")


for k in range(len(pt)):
    if pt[k] % 2 != 0:
        if a1 != 0 and a2 != 0:
            a1 = 0
            a2 = 0
            break
        elif a1 != 0:
            a2 = pt[k]
        else:
            a1 = pt[k]
if a1 != 0 and a2 != 0:
    print(a1)
    print(a2)
    print("Есть 2 нечетных пятизначных числа")

