N = int(input())
sum = 0
cnt = 0
c = 1
while sum < N:
    cnt = sum
    sum += c
    c += 1
if c%2==0:
    print(f'{c-(N-cnt)}/{N-cnt}')
else:
    print(f'{N-cnt}/{c-(N-cnt)}')
