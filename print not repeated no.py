k1=int(input())
k2=list(map(int,input().split()))
for i in k2:
  if k2.count(i)<=1:
    print(i)
