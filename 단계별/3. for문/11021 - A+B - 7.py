import sys

T = int(input())

# result = []
# for i in range(T):
#     A,B = map(int,sys.stdin.readline().split())
#     result.append(A+B)

# for i in range(T):
#     print('Case #{}: {}'.format(i+1,result[i]))


for i in range(T):
    A,B = map(int,sys.stdin.readline().split())
    print(f'Case #{i+1}: {A+B}')