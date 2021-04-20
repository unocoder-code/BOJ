T = int(input())

for _ in range(T):
    H = int(input())
    W = int(input())
    room = [val for val in range(1,W+1)]
    for i in range(H):
        for j in range(1,W):
            room[j] += room[j-1]
    print(room[W-1])
