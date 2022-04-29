N,K = map(int,input().split())
a=[]
for i in range(1,N+1):
    if N%i ==0:
        a.append(i)

if len(a)<K:
    print(-1)
else:   
    print(a[K-1])