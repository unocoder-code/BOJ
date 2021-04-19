a_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

S = input()
num = []
for i in a_list:
    num.append(S.count(i))

print(len(S)-sum(num))