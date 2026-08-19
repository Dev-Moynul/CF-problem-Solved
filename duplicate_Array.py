n = int(input())
arr = list(map(int, input().split()))
ans = []
for i in range(n):
    if arr[i] not in arr[i+1:]:
        ans.append(arr[i])
print(len(ans))
print(*ans)