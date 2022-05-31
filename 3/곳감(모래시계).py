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
                p = k-count+N
            else:
                p = k-count
            a[b[i][0]-1][p] = temp[k]   
    elif b[i][1]==1:
        for k in range(N):
            if (k+count)>N-1:
                p = k+count-N
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
    



# import sys
# sys.stdin = open("in1.txt","rt")

# n=int(input())
# a=[list(map(int,input().split())) for _ in range(n)]

# m=int(input())
# for i in range(m):
#     h,t,k = map(int,input().split())
#     if t==0:
#         for _ in range(k):
#             a[h-1].append(a[h-1].pop(0)) #pop(0)하면 맨 앞에거가 빠지고 알아서 땡겨지나봄
#     else:
#         for _ in range(k):
#             a[h-1].insert(0,a[h-1].pop()) 


# res = 0
# s = 0
# e = n-1
# for i in range(n):
#     for j in range(s, e+1):
#         res+=a[i][j]
#     if i<n//2:
#         s+=1
#         e-=1
#     else:
#         s-=1
#         e+=1

