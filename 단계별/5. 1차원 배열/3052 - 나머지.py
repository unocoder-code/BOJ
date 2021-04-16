array =[]
for i in range(10):
    x = int(input())%42
    if x not in array:
        array.append(x)

print(len(array))