# import sys
# sys.stdin = open("in5.txt","r")

# N,M = map(int,input().split())
# a = list(map(int,input().split()))
# a.sort()
# b = k = N//2

# while True:
#     if a[k]<M:
#         b=(b//2)+1
#         k += b
#     elif a[k]>M:
#         b=b//2
#         k = b
#     else :
#         print(k+1)
#         break

import sys
sys.stdin = open("in5.txt","r")

N,M = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

lt = 0
rt = N-1
while lt<=rt:
    mid = (lt+rt)//2
    if a[mid]==M:
        print(mid+1)
        break
    elif a[mid]>M:
        rt = mid-1
    else:
        lt = mid+1