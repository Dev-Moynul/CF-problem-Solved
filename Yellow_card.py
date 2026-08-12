a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())
r = n

sc= a1 * (k1 - 1) + a2 * (k2 - 1)
minimum = max(0, n - sc)
mxm = 0
if k1 > k2:
    a1, a2 = a2, a1
    k1, k2 = k2, k1

x = min(a1, n // k1)
mxm += x
n -= x * k1

x = min(a2, n // k2)
mxm += x

print(minimum, mxm)