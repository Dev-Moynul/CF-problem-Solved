import sys
from collections import Counter
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))

    cnt = Counter(b)
    s = sorted(cnt.keys())
    if s[0] != 0:
        print(-1)
        continue
    r = {}
    pv = 0
    ok = True
    m = len(s)
    for i in range(m - 1):
        cur = s[i]
        nxt = s[i + 1]
        freq = cnt[cur]
        diff = nxt - cur
        if diff % freq != 0:
            ok = False
            break
        v = diff // freq

        if v <= pv:
            ok = False
            break
        r[cur] = v
        pv = v
    if not ok:
        print(-1)
        continue
    if m == 1:
        r[0] = 1
    else:
        r[s[-1]] = pv + 1
    ans = [str(r[x]) for x in b]
    print(*ans)