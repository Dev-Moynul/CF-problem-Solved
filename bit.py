import sys
input = sys.stdin.readline
x = 0
for _ in range(int(input())):
    n = (input())
    if "++" in n:
        x +=1
    else:
        x -=1
print(x)