for _ in range(int(input())):
    a, b, t= map(int, input().split())
    if t == 1:
        print(a)
    elif t == 2:
        print(b)
    else:
        print(a & b)