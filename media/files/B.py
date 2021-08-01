n = int(input())

mmax = 0
cur = 0
for i in range(n):
    a = int(input())
    if a == 1:
        cur += 1
    else:
        if cur > mmax:
            mmax = cur
        cur = 0
    if i == n - 1 and cur > mmax:
        mmax = cur
print(mmax)
