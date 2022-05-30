# import sys
# sys.stdin = open("in1.txt","rt")

# N, M = map(int, input().split())

# a = list(map(int,input().split()))

# count=0
# add=0
# for i in range(0,N):
#     for j in range(i, N):
#         if i==j:
#             add += a[j]
#             if add<M:
#                 continue
#             elif add==M:
#                 count+=1
#                 add=0
#                 break
#             else :
#                 add=0
#                 break

#         else:
#             add += a[j]
#             if add<M:
#                 continue
#             elif add==M:
#                 count+=1
#                 add=0
#                 break
#             else :
#                 add=0
#                 break

# print(count)


# import sys
# sys.stdin = open("in2.txt", "r")
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# lt=0
# rt=1
# tot = a[0]
# cnt = 0
# while True:
#     if tot<m:
#         if rt<n:
#             tot += a[rt]
#             rt+=1
#         else: 
#             break
#     elif tot==m:
#         cnt+=1
#         tot-=a[lt]
#         lt+=1
#         print(lt,rt)
#     else:
#         tot-=a[lt]
#         lt+=1
# print(cnt)

import sys
sys.stdin = open("in2.txt","r")

N,M = map(int, input().split())
a = list(map(int,input().split()))
count = 0
add=0
for i in range(N):
    add += a[i]
    if add==M:
        count+=1
        add=0
        print(i)
    else:
        for j in range(i+1, N):
            add += a[j]

            if add==M:
                count+=1
                add=0
                print(i,j)
                break
            elif add>M:
                add=0
                break
            else:
                if j==N-1:
                    add=0
                    break
                continue
print(count)

        