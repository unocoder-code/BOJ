import sys

T = int(input())

for i in range (T):
    total = 0
    num = 0
    A = list(map(int,sys.stdin.readline().split()))
    x = A.pop(0)
    total = sum(A)/x
    for a in A:
        if a>total:
            num += 1
    print(f'{num/x*100:.3f}%')