import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = (input())
    x = 0
    if "++" in n:
        x +=1
    else:
        x -=1
print(x)