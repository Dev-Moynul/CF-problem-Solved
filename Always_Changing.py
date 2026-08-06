import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    cnt0 = s.count('0')
    cnt1 = n - cnt0
    ans = float('inf')
    for srt in ['0', '1']:
        ext = srt
        seq = []
        for c in s:
            if c == ext:
                seq.append(c)
                ext = '1' if ext == '0' else '0'
        k0 = seq.count('0')
        k1 = seq.count('1')

        while True:
            d0 = cnt0 - k0
            d1 = cnt1 - k1
            if abs(d0 - d1) <= 1:
                ans = min(ans, d0 + d1)
            if not seq:
                break
            x = seq.pop()
            if x == '0':
                k0 -= 1
            else:
                k1 -= 1
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)