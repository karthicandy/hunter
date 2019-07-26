k1,k2=list(map(int,input().split()))
k3=list(map(int,input().split()))
k3.sort()
k3=k3[::-1]
print(k3[k2-1])
