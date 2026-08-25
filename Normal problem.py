for _ in range(int(input())):
    n = input().strip()
    r =""
    for ch in reversed(n):
        if ch == "p":
            r += "q"
        elif ch == "q":
            r += "p"
        else:
            r += "w"
    print(r)