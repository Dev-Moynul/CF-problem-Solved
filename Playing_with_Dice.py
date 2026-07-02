import sys
input = sys.stdin.readline

a, b = map(int, input().split())

f = 0
d = 0
s = 0

for i in range(1, 7):
    d1 = abs(a - i)
    d2 = abs(b - i)

    if d1 < d2:
        f += 1
    elif d1 == d2:
        d += 1
    else:
        s += 1

print(f, d, s)