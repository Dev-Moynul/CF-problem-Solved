for _ in range(int(input())):
    n, a, b = map(int, input().split())

    cost = min(2 * a, b)

    ans = (n // 2) * cost + (n % 2) * a

    print(ans)