N = int(input())

for i in range (N):
    x = input()
    score = 0
    total = 0
    for i in x:
        if i == 'O':
            score +=1
            total += score
        else:
            score = 0
    print(total)