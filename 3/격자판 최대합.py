# import sys
# sys.stdin = open("in1.txt","rt")

# N = int(input())

# m = [[0]*N for i in range(N)]
# #m = [[0 for col in range(N)] for row in range(N)]
# for i in range(N):
#     m[i] = (list(map(int, input().split())))

# #각 row ㅡ 의 합 중 max
# r_max=0
# for i in range(N):
#     sum=0
#     for j in range(N):
#         sum+=m[i][j]
#     if r_max<sum:
#         r_max = sum

# c_max=0
# for i in range(N):
#     sum=0
#     for j in range(N):
#         sum+=m[j][i]
#     if c_max<sum:
#         c_max = sum

# sum=0
# a_max=0
# for i in range(N):
#     sum+=m[i][i]
# a_max = sum

# sum=0
# b_max=0
# for i in range(N):
#     sum+=m[N-1][N-i-1]
# b_max = sum

# print(max(r_max,c_max,a_max,b_max))

# import sys
# sys.stdin = open("in1.txt")

# n = int(input())
# a = [list(map(int,input().split())) for _ in range(n)]

# largest = -2147000000
# for i in range(n):
#     sum1=sum2=0
#     for j in range(n):
#         sum1+=a[i][j]
#         sum2+=a[j][i]
#     if sum1>largest:
#         largest = sum1
#     if sum2>largest:
#         largest = sum2

# for i in range(n):
#     sum1+=a[i][i]
#     sum2+=a[i][n-i-1]
#     if sum1>largest:
#         largest = sum1
#     if sum2>largest:
#         largest = sum2

# print(largest)
