for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ng = a.count(-1)
    z = a.count(0)
    r = z
    if n % 2 == 1:
        r += 2
    print(r)    