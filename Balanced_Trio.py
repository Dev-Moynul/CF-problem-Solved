import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b, c = map(int, input().split())

    s = a + b + c

    if s % 2:
        print("No")
        continue

    need = s // 2

    a1 = min(a, need)
    need -= a1

    b1 = min(b, need)
    need -= b1

    c1 = min(c, need)
    need -= c1

    a2 = a - a1
    b2 = b - b1
    c2 = c - c1

    print("Yes")
    print(a1, b1, c1, a2, b2, c2)