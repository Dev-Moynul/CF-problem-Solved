import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    ans = []
    for i in range(1, n + 1):
        ans.append(i)
    for i in range(1, n + 1):
        ans.append(i)
    for i in range(2, n + 1):
        ans.append(i)
    ans.append(1)

    for i in range(1, n + 1):
        ans.append(i)

    print(*ans)