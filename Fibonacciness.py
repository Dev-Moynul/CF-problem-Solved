import sys
from collections import Counter
input = sys.stdin.readline

for _ in range(int(input())):
    a1, a2, a4, a5 = map(int, input().split())

    vals = [
        a1 + a2,
        a4 - a2,
        a5 - a4
    ]
    cnt = Counter(vals)
    sys.stdout.write(str(max(cnt.values())) + '\n')