#Найдите сумму 1+11+111+1111+...1111...1, если последнее слагаемое состоит из n цифр.
n = int(input())
result = 0
a = "1"
for i in range(n):
    result += int(a)
    a += "1"
print(result)
