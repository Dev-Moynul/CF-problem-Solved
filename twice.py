from collections import Counter
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = Counter(a)

    r = 0
    for i in cnt.values():
        r += i // 2 
    print(r)