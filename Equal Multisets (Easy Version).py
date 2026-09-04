import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ok = True
    for i in range(n):
        if i < n - k or i >= k:
            if b[i] != -1 and b[i] != a[i]:
                ok = False
                break
    if not ok:
        print("NO")
        continue
    need = set(a[n-k:k])
    for i in range(n-k, k):
        if b[i] != -1:
            if b[i] not in need:
                ok = False
                break
            need.remove(b[i])
    print("YES" if ok else "NO")