n, k = map(int, input().split())
a = list(map(int, input().split()))
r = a[k-1]
c = 0
for s in a:
    if s >= r and s > 0:
        c +=1
print(c)