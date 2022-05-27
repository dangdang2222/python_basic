import sys
sys.stdin = open("in1.txt","rt")

N = int(input())
a = [[0]*N for i in range(N)]
for i in range(N):
    a[i] = list(map(int,input().split()))

M = int(input())
b = [[0]*M for i in range(M)]
for i in range(M):
    b[i] = list(map(int,input().split()))

for i in range(M):
    temp = a[b[i][0]-1][:]
    count = b[i][2]

    if b[i][1]==0:
        for k in range(N):
            if (k-count)<0:
                p = k-count+5
            else:
                p = k-count
            a[b[i][0]-1][p] = temp[k]   
    elif b[i][1]==1:
        for k in range(N):
            if (k+count)>4:
                p = k+count-5
            else:
                p = k+count
            a[b[i][0]-1][p] = temp[k]

count=0
for i in range(int(N/2)):
    count += sum(a[i][i:N-i])
count += a[int(N/2)][int(N/2)]
for i in range(int(N/2)):
    count += sum(a[N-1-i][i:N-i])
print(count)
    



