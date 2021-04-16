def d(n):
    X = str(n)
    total = n
    for i in X:
        total += int(i)
    return total

A = []
for N in range (1,10001):
    A.append(d(N))

for i in range (1,10001):
    if i in A:
        pass
    else:
        print(i)