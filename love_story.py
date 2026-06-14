import sys
input = sys.stdin.readline
target = "codeforces"
for _ in range(int(input())):
    s = input().strip()
    c = 0
    for i in range(10):
        if s[i] != target[i]:
            c += 1
    sys.stdout.write(str(c) + '\n')