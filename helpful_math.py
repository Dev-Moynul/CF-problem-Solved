import sys
input  = sys.stdin.readline

s = input().strip()
arr = s.split("+")
arr.sort()
print("+".join(arr))