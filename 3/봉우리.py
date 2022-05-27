import sys
sys.stdin = open("in1.txt","rt")

N = int(input())
a = [[0]*(N+2) for i in range(N+2)]


b = [[0]*(N) for i in range(N)]
for i in range(N):
    b[i] = list(map(int,input().split()))

for i in range(N+2):
    for k in range(N+2):
        if i==0 or k==0 or i==N+1 or k==N+1: continue
        else:
            a[i][k] = b[i-1][k-1]
count = 0
for i in range(1,N+1):
    for k in range(1,N+1):
        if max(a[i][k],a[i-1][k],a[i+1][k],a[i][k+1],a[i][k-1]) == a[i][k]:
            count+=1
print(count)