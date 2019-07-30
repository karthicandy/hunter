k1=int(input())
k2=list(map(int,input().split()))
k3=[]
for i in k2:
  if i not in k3:
    k3.append(i)
print(*sorted(k3))
