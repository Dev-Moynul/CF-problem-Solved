import sys
input = sys.stdin.readline

for _ in range(int(input())):

    a, b, c, n = map(int, input().split())

    mx = max(a, b, c)
    need = (mx - a) + (mx - b) + (mx - c)
    
    if need <= n and (n - need) % 3 == 0:
        print("YES")
    else:
        print("NO")