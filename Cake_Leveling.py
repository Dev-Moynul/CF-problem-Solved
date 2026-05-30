t=int(input())
for _ in range(t):
    n= int(input())
    a=list(map(int, input().split()))
    pref=0
    mn=10**18
    result=[]
    for i in range(n):
        pref+=a[i]
        mn=min(mn, pref // (i + 1))
        result.append(str(mn))
    print(*result)