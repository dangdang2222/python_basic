N,K = map(int,input().split())
print(N,K)
a=[]
for i in range(1,N+1):
    if N%1 ==0:
        a.append(i)

a.sort()
print(a[K-1])