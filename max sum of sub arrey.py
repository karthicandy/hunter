k2=int(input())
k1=list(map(int,input().split()))[:k1]
k3=list(map(int,(k1)))
x=0
for i in k1:
  x=x+i
  k3.append(x)
k3.sort()
print(k3[-1])
