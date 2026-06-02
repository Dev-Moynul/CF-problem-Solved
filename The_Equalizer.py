t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    if (n * k) % 2 == 0:
        print("YES")
    else:
        print("YES" if s % 2 == 1 else "NO")