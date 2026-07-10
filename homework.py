from collections import deque

t = int(input())

for _ in range(t):
    input()
    d = deque(input())

    m = int(input())
    b = input()
    c = input()

    for i in range(m):
        if c[i] == 'V':
            d.appendleft(b[i])
        else:
            d.append(b[i])

    print("".join(d))