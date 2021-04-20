import math
N = int(input())
for i in range(N):
    A,B = map(int,input().split())
    D = B-A
    x = int(math.sqrt(D))
    nam = D-(x**2)
    print(x*2-1 + nam//x if nam%x==0 else x*2-1 + nam//x +1)