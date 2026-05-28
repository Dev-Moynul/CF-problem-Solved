t = int(input())
for _ in range(t):
    n = int(input())
    result = 1
    while n>3:
        result *= 2
        n //=4
    print(result)