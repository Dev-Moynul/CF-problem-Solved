l,r =map(int, input().split())
a, b = 0, 1
if l<=0<=r:
    print(0)
if l<=1 <=r:
    print(1)
while True:
    c=a+b
    if c>r:
        break
    if c>=l:
        print(c)
    a, b = b, c