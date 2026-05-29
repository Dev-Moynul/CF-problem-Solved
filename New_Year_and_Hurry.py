n, k = map(int, input().split())
a = 240 - k
s = 0
c = 0
for i in range(1,n+1):
    s += 5*i
    if s <= a:
        c += 1
    else:
        break
print(c)