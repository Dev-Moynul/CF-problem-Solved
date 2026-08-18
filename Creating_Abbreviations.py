for _ in range(int(input())):
    a, b = map(int, input().split())
    s = set()
    for _ in range(a):
        s.add(input()[0])
    l = []
    for _ in range(b):
        l.append(input().lower())
    flag = True
    for w in l:
        for ch in w:
            if ch not in s:
                flag = False
                break
    if flag:
        print("YES")
    else:
        print("NO")
     