def d(N):
    num = 0
    for n in range (1,N+1):
        X = str(n)
        sub = []
        for i in range (len(X)-1):
            sub.append(int(X[i]) - int(X[i+1]))
        if a(sub):
            num += 1
    return num

def a(sub : list):
    for i in range (len(sub)-1):
        if sub[i] != sub[i+1]:
            return False
        else:
            pass
    return True
                
x = int(input())
print(d(x))