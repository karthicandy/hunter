k4=list(str(input()))
k5=[]
for i in k4:
  if i not in k5:
    k5.append(i)
print(*k5,sep="")
