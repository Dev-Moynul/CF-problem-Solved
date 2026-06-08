import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mn = min(a)
    mx = max(a)
    sys.stdout.write(str((mx - mn + 1) // 2) + "\n")