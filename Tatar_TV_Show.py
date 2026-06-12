import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip()
    result = True
    for r in range(k):
        c = 0
        for i in range(r, n, k):
            if s[i] == '1':
                c += 1
        if c % 2 == 1:
            result = False
            break
    print("YES" if result else "NO")