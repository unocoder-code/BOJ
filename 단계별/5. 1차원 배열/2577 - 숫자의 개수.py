A = int(input())
B = int(input())
C = int(input())

X = str(A*B*C)

for i in range (10):
    i = str(i)
    print(X.count(i))