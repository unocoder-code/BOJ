N = int(input())
result = 0
array = input()
for i in range (N):
    result += ord(array[i])-48

print(result)