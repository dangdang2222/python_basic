import sys
#sys.stdin=open("in2.txt","rt")
#시간초과
n = int(input())

count=n
check=0
for i in range(2,n+1):
    for j in range(1,i+1):
        if i%j==0:
            if j!=i and j!=1:
                count-=1
                break
print(count-1)




# n = int(input())
# ch = [0]*(n+1)
# cnt=0

# for i in range(2,n+1):
#     if ch[i]==0:
#         cnt+=1
#         for j in range(i,n+1,i): #step 주의
#             ch[j]=1

# print(cnt)