l,r = map(int, input().split())

a, b = 0, 1
one = False
while a <= r:
    if a >= l:
        if a == 1:
            if not one:
                print(1)
                one = True
        else:
            print(a)

    a, b = b, a + b