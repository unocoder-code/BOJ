A, B, C = map(int, input().split())
i = 0
if B>=C:
    print(-1)
else:
    x = A//(C-B)
    print(x+1)