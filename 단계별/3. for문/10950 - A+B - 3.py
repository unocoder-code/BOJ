T = int(input())
result = []
for i in range (T):
    A, B = map(int,input().split())
    result.append(A+B)

for i in range (T):
    print(result[i])