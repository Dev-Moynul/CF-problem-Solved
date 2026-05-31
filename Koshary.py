t = int (input())
x, y = map(int,input().split())
for _ in range(t):
    if x % 2 == 1 and y % 2 == 1:
        print('NO')
    else:
        print('YES')