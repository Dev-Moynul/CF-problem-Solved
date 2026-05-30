t = int(input())

for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    m = c[n // 2]

    l= 0
    g = 0
    for x in c:
        if x < m:
            l += 1
        elif x > m:
            g += 1
    print(max(l, g))