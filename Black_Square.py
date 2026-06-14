import sys
input = sys.stdin.readline
a = list(map(int, input().split()))
s = input().strip()
c = 0
for i in s:
    c += a[int(i) - 1]
sys.stdout.write(str(c) + '\n')