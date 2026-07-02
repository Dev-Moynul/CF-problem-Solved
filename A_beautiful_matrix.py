import sys
input = sys.stdin.readline

for i in range(5):
    arr = list(map(int, input().split()))

    if 1 in arr:
        j = arr.index(1)
        print(abs(i - 2) + abs(j - 2))
        break