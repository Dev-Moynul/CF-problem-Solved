n = int(input())
s = list(map(int,input().split()))
h = s[0]
l = s[0]
c = 0
for i in range(1,n):
    if s[i]>h:
        c += 1
        h = s[i]
    elif s[i]<l:
        c +=1
        l = s[i]
print(c)  
