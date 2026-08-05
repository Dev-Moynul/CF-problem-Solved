import sys
input = sys.stdin.readline
c = 0
m = 0
for _ in range (int(input())):
    a, b = map(int, input().split())
    c -= a
    c += b
    m = max(m, c)
print(m)