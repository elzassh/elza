#№4
word = sorted("автор")
alternative = ["товар"]
for a in alternative:
    if word == sorted(a):
        print(a)

#№6
a = [1,2,3,4,5,6,7]
x = 9
for i in range(len(a)-1):
    if (a[i] + a[i+1]) == x:
        print(a[i],a[i+1])

#№7
a = ("safari")[::-1]
print(a)

#№8
a = "bj iy"
if a != a[::-1]:
    print("not palindrome")
else:
    print("palindrome")

#№8.1
a = "bob"
if a != a[::-1]:
    print("not palindrome")
else:
    print("palindrome")
