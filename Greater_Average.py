t = int(input())
for _ in range(t):
    a, b, c = map(float, input().split())
    if (a+b)/2 > c:
        print('YES')
    else:
         print('NO')