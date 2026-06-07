t = int(input())
p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 11]
for _ in range(t):
    n = int(input())
    if n == 10:
        print(-1)
    elif n < 10:
        print(n, 0)
    elif n == 11:
        print(11, 0)
    else:
        a = p[n % 12]
        print(a, n - a)