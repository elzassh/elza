#4. Подсчитать количество цифр в числе n
n = int(input("Введите число:"))
a = 0
while(n > 0):
    a += 1
    n = n // 10
print(a)
