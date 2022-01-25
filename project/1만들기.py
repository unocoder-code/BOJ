N, K = map(int,input().split())

count = 0
# while N!=1:
#   N = N//K if N%K==0 else N-1
#   count+=1

while True:
  target = N//K*K
  count += (N-target)
  N = target
  if N<K:
    break
  count+=1
  N //=K

count += (N-1)
print(count)
