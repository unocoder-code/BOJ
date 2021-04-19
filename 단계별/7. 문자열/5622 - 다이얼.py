result = 0
array = input()

for i in array:
    if ord(i)<80:
        result += (ord(i)-56)//3
    elif ord(i)<84:
        result += 8
    elif ord(i)<87:
        result += 9
    else:
        result += 10 

print(result)