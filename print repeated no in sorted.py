k1=int(input())
k2=list(map(int,input().split()))
k3=[]
for i in k2:
  if k2.count(i)>1:
    if i not in k3:
      k3.append(i)
if len(k3)>=1:
  print(*sorted(k3))
else:
  print('unique')
