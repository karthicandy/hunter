k4=int(input())
k1=list(map(int,input().split()))
k=1
for i in k1:
  k*=i
for j in k1:
  j=k/j
  print(int(j),end=" ")
