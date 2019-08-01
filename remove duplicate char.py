k1=list(str(input()))
k2=[]
for i in k1:
  if i not in k2:
    k2.append(i)
print(*k2,sep="")
