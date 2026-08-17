import sys 
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    r = a[0] + n - 1
    s = b[0] + n - 1

    if s <= r:
        print(1)
    else:
        print(2)