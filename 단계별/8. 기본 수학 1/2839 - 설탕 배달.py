N = int(input())
sum = -1
for i in range(N//5,-1,-1):
    if (N-5*i)%3==0:
        sum = i+(N-5*i)//3
        break
print(sum)