k1=int(input())
k2=list(map(int,input().split()))[:k1]
k3=list(map(int,(k2)))
x=0
for i in k2:
  x=x+i
  k3.append(x)
k3.sort()
print(k3[-1])
