N = int(input())
Score = list(map(int,input().split()))
Max = 0
total = 0

for i in Score:
    total += i
    if Max <= i:
        Max = i

print((total/N)*100/Max)