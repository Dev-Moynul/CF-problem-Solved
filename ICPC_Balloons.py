t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    solved = set()
    balloons = 0
    for ch in s:
      if ch not in solved:
        balloons +=2
        solved.add(ch)
      else:
        balloons += 1
    print(balloons)