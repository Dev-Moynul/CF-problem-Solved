a, b = map(int,input().split())
l = 1
h = a
cnt = 0
while l < h:
    mid = (l+h)//2
    cnt += 1
    if b > mid:
        l = mid + 1
    else:
        h = mid
print(cnt)