N,K = map(int,input().split())
a=[]
for i in range(1,N+1):
    if N%i ==0:
        a.append(i)

if len(a)<K:
    print(-1)
else:   
    print(a[K-1])


'''
import sys
sys.stdin=open("input.txt","rt")

n,k = map(int,input().split())
cnt=0
for i in range(1,n+1):
    if n%1==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)
'''