k4=list(str(input()))
k5=[]
for k in k4:
  if k not in k5:
    k5.append(k)
print(*k5,sep="")
