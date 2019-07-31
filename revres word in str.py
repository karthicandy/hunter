k1=list(map(str,input().split()))
k2=[]
for i in k1:
  k3=i[::-1]
  k2.append(k3)
print(*k2)
