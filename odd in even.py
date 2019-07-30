k1=int(input())
k2=list(map(int,input().split()))
k3=[]
for i in range(k1):
  if i%2==0:
    if k2[i]%2!=0:
      k3.append(k2[i])
  elif i%2!=0:
    if k2[i]%2==0:
      k3.append(k2[i])
print(*(k3))
