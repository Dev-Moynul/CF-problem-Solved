import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b = map(int, input().split())

    if b >= 3 * a:
        print(n * a)
        continue

    g = n // 3
    rem = n % 3

    ans = g * b

    if rem == 1:
        ans += min(a, b)
    elif rem == 2:
        ans += min(2 * a, b)

    print(ans)