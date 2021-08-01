n = int(input())

if n != 0:
    a = int(input())
    prev = a
    print(a)
for i in range(n - 1):
    a = int(input())
    if prev != a:
        print(a)
        prev = a
