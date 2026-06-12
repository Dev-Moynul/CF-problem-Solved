import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    mx = max(h)
    mn = min(h)
    print ( mx+1-mn)