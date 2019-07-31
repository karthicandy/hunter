k1=list(str(input()))
if (k1==k1[::-1]):
  del(k1[-1])
  print(*k1,sep="")
else:
  print(*k1,sep="")  
