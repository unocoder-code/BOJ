import sys
print(max([int(e[::-1]) for e in list(sys.stdin.readline().split())]))

# import sys
# array = list(map(str,sys.stdin.readline().split()))
# print(max(int(array[0][::-1]),int(array[1][::-1])))