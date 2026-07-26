import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))

    if n % 2 == 1:
        print("NO")
        continue

    mn = 10 ** 18
    mx = -1

    for i in range(n):
        if i % 2 == 0:      # position 1,3,5...
            mn = min(mn, w[i])
        else:               # position 2,4,6...
            mx = max(mx, w[i])

    if mx + 1 < mn:
        print("YES")
    else:
        print("NO")