import sys

T = int(input())
for i in range(T):
    A,B = map(str,sys.stdin.readline().split())
    for i in range(len(B)):
        print(B[i]*(ord(A)-48),end='')
    print()