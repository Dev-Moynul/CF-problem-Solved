import sys
input = sys.stdin.readline
u = 0
l = 0
s = input()
for ch in(s):
    if ch.isupper():
        u += 1
    else:
        if ch.islower():
            l +=1
if l > u:
    print(s.lower())
else:
    print(s.upper())