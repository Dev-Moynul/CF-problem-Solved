from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = Counter(a)

    ans = 0
    for x in cnt.values():
        ans += x // 2

    print(ans)