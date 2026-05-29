l , r = map(int, input().split())
a , b = 0, 1
while a<=r:
    if a>=l:
        print(a)
    c=a+b
    a=b
    b=c