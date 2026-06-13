import sys
input = sys.
n, m = map(int, input().split())

ans = 0

for a in range(32):
    b = n - a * a

    if b >= 0 and a + b * b == m:
        ans += 1

print(ans)