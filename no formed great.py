k1=input()
k2=list(map(int,input().split()))
k2.sort(reverse=True)
for i in k2:
  if k2[0]==0:
    print(0)
    break
  print(i,end="")
