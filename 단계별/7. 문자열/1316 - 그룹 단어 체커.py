import sys
N = int(input())
for _ in range(N):
    S = sys.stdin.readline()
    for i in range(1, len(S)):
        if S.find(S[i-1]) > S.find(S[i]):
            N -= 1
            break
print(N)

# import sys

# N = int(input())
# for i in range(N):
#     X = 0
#     S = sys.stdin.readline()
#     S_set = list(set(S))
#     for a in S_set:
#         index_list = list(filter(lambda x: S[x] == a, range(len(S))))
#         if len(index_list) == 1:
#             continue
#         else:
#             for j in range(len(index_list)-1):
#                 if index_list[j] + 1 != index_list[j+1]:
#                     X = -1
#                     break
#     if X == -1:
#         N -=1
# print(N)