from collections import deque

def bfs():
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i,j))
    while queue:
        x, y = queue.popleft()
        for e in range(4):
            nx = x + dx[e]
            ny = y + dy[e]
            if nx<0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
       
m, n = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

bfs()
res = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res,max(i))

print(res-1)