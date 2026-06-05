MOD = 676767677

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    b = list(map(int, input().split()))

    sz = [0] * m
    for x in b:
        sz[x] += 1

    ans = 1
    seated = sz[0]
    ok = True

    for level in range(1, m):

        for i in range(n):
            if b[i] != level:
                continue

            good = False

            if i > 0 and b[i - 1] < level:
                good = True

            if i + 1 < n and b[i + 1] < level:
                good = True

            if not good:
                ok = False
                break

        if not ok:
            break

        ans = (ans * pow(seated, sz[level], MOD)) % MOD
        seated += sz[level]

    print(ans if ok else 0)