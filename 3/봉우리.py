import sys
sys.stdin = open("in3.txt","rt")

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
        if max(a[i-1][k],a[i+1][k],a[i][k+1],a[i][k-1]) < a[i][k]:
            count+=1
print(count)


#이거 답이 잘못된거 아님?
#일단 격자판 최대합까지는 답 확인함
#봉우리,수들의 합 틀림

# import sys
# sys.stdin = open("in3.txt","rt")

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# n=int(input())
# a=[list(map(int,input().split())) for _ in range(n)]
# a.insert(0, [0]*n) #맨 위에 넣기
# a.append([0]*n) #맨 밑에 넣기
# for x in a:
#     x.insert(0,0)
#     x.append(0)

# cnt = 0

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)): #모두가 다 참일때 참
#             cnt+=1
# print(cnt)
