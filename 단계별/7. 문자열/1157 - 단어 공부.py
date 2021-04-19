s = input().upper()
cnt = list(map(s.count,map(chr,range(65,91))))
if cnt.count(max(cnt))==1:
   print(chr(cnt.index(max(cnt))+65))
else:
    print("?")


# S = input()
# max = ['',0,'o']
# for i in range(26):
#     lar = chr(i+65)
#     small = chr(i+97)
#     num = S.count(lar) + S.count(small)
#     if max[0] != lar:
#         if num > max[1]:
#             max = [lar,num,'o']
#         elif num == max[1]:
#             max = [lar,num,'?']
#     else:
#         pass
# if max[2]=='o':
#     print(max[0])
# else:
#     print('?')