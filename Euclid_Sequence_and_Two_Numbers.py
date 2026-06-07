t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    if n == 2:
        print(max(b), min(b))
        continue
    a = sorted(b, reverse=True)
    ok = True
    for i in range(2, n):
        if a[i - 2] % a[i - 1] != a[i]:
            ok = False
            break
    if ok:
        print(a[0], a[1])
    else:
        print(-1)