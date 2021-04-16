A = []
Max = 0
for i in range (9):
    A.append(int(input()))
    if Max <= A[i]:
        Max = A[i]

print(Max)
print(A.index(Max)+1)