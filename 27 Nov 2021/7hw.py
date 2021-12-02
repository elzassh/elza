#7. Вводится число n. Найти максимальную цифру среди цифр числа.
n = input()
max_n = 0
for i in range(len(n)):
    ni = int(n[i])
    if ni > max_n:
        max_n = ni
print(max_n)