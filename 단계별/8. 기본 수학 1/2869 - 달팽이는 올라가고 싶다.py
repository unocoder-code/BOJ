A, B, V = map(int,input().split())
x = (V-A)/(A-B)
if x == int(x):
    print(int(x)+1)
else:
    print(int(x)+2)

# cur = 0
# day = 0
# while cur < V:
#     cur += A
#     day += 1
#     if cur >= V:
#         break
#     cur -=B
# print(day)
