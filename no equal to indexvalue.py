k1=int(input())
k2=list(map(int,input().split()))
x=0
j=0
for i in k2:
  if i==j:
    print(i,end=" ")
    x+=1
  j+=1
if x==0:
  print(-1)
