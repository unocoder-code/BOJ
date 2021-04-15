N = int(input())
X = N
i = 0
while True:
    i += 1
    M = int(N/10) + int(N%10)
    N = (N%10)*10 + (M%10)

    if X == N:
        print(i)
        break