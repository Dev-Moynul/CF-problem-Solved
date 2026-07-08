import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    if len(s) <=10:
        print(s)
    else:
        a = s[0]
        b = s[-1]
        c = len(s)-2
        print(a + str(c) + b)