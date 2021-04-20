T = int(input())
for _ in range(T):
    H,W,N = map(int,input().split())
    num = N//H + 1
    flo = N%H
    if N%H==0:
        num-=1
        flo=H
    print(f'{flo}0{num}' if num<10 else f'{flo}{num}')