dx = [0, -1, 0 ,1]
dy = [1, 0, -1, 0]

x, y = 2, 2

for i in range(4):
  #다음위치
  nx = x + dx[i]
  ny = y + dy[i]
  print(nx, ny)

#############좌표_아동#################3

N = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1 ,1]
dy = [-1, 1, 0, 0]
move_types = ['L','R','U','D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx<1 or ny<1 or nx>N or ny>N:
    continue
  x,y = nx, ny

print(nx, ny)

###########왕실의 나이트###############
spot = input()
row = int(spot[1])
column = int(ord(spot[0])) - int(ord('a')) + 1

steps = [(-2,-1),(-2,1),(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]

  if next_row>=1 and next_column>=1 and next_row<=8 and next_column<=8:
    result+=1

print(result) 