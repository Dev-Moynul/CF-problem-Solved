n, k, l, c, d, p, nl, np = map(int, input().split())
drink = (k*l)//n
lime = c*d
salt = p//np
print(min(drink, lime, salt)//n)