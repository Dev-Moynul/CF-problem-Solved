for _ in range(int(input())):
    m, a, b, c = map(int, input().split())
    r1 = min(a, m)
    r2 = min(b, m)
    e = (m - r1) + (m - r2)
    ans = min(c, e)
    print(ans + r1 + r2)
