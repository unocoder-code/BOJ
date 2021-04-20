
N=int(input())
sum=1
c=1

while N > sum:
  sum += 6*c
  c+=1
  
print(c)

# 1 - 1                 1
# 2 - 2~7 - 6           
# 3 - 8~19 -18          2
# 4 - 20~37 -36         3
# 5 - 38~61 -60         4