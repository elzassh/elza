n = int(input())
n = str(n)
result = 0
a = 0
for i in range(len(n)-1,-1,-1):
    if a % 2 == 0:
        result += int(n[i])
    elif a % 2 != 0:
        result -= int(n[i])
    a += 1

print(result)
