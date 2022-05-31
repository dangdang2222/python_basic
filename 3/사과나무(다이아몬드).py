from html.entities import name2codepoint
import sys
sys.stdin = open("in1.txt","rt")

N = int(input())
b = list()
for i in range(N):
    a = list(map(int,input().split()))
    b.append(a)
count=0
for i in range(int(N/2)):
    count+=sum(b[i][int(N/2)-i:int(N/2)+i+1])
count+=sum(b[int(N/2)][:])
for i in range(int(N/2)):
    count+=sum(b[int(N/2)+1+i][i+1:N-i-1])

print(count)    

# import sys
# sys.stdin = open("in1.txt","rt")

# n = int(input())
# a = [list(map(int,input().split())) for _ in range(n)]
# res = 0

# s=e=n//2
# for i in range(n):
#     for j in range(s, e+1):
#         res+=a[i][j]
#     if i<n//2:
#         s-=1
#         e+=1
#     else:
#         s+=1
#         e-=1