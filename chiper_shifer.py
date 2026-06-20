for _ in range(int(input())):
    n = int(input())
    s = input()

    ans = ""
    i = 0

    while i < n:
        ch = s[i]
        ans += ch
        i += 1

        while s[i] != ch:
            i += 1

        i += 1

    print(ans)