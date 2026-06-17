import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    vals = sorted(100 // x for x in a)
    reach = 0
    ok = True

    for v in vals:
        if v > reach + 1:
            ok = False
            break
        reach += 100

    print("Yes" if ok else "No")