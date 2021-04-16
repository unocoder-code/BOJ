N = int(input())
array = list(map(int,input().split()))

Max = array[0] ; Min = array[0]

for i in array:
    if Max<=i:
        Max = i
    if Min>=i:
        Min = i

print(Min,Max)