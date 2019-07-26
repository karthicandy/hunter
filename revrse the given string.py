k1,k2=list(map(int,input().split()))
k3=list(map(str,input().split()))
k3.sort(reverse=True)
print(k3[k2-1])
