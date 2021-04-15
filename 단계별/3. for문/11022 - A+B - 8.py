import sys

T = int(input())

# result = []
# for i in range(T):
#     A,B = map(int,sys.stdin.readline().split())
#     result.append([A,B,A+B])

# for i in range(T):
#     print(f'Case #{i+1}: {result[i][0]} + {result[i][1]} = {result[i][2]}')

for i in range(T):
    A,B = map(int,sys.stdin.readline().split())
    print(f'Case #{i+1}: {A} + {B} = {A+B}')