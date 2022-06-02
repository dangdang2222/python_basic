import sys
from this import d
sys.stdin = open("in5.txt","r")

n,c = map(int,input().split())
a=[]
for i in range(n):
    a.append(int(input()))
a.sort()

def distance(k):
    cnt=1
    i=0
    while i<n:
        first = a[i]
        for j in range(i+1,n):
            if (a[j]-a[i])>=k:
                cnt+=1
                i = j
        if j==n-1:
            break
 
    #print(k,cnt)
    if cnt>=c:
        return True
    else:
        return False

lt = 1
rt = a[n-1]-a[0]
res=0
while lt<=rt:
    mid = (lt+rt)//2
    if distance(mid)==True:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)


# n,c = map(int,input().split())
# Line = []
# for _ in range(n):
#     tmp = int(input())
#     Line.append(tmp)
# Line.sort()

# lt=1
# rt=Line[-1]-Line[0]

# def Count(len):
#     cnt=1
#     ep=Line[0]
#     for i in range(1,n):
#         if Line[i]-ep>=len:
#             cnt+=1
#             ep = Line[i]
    
#     return cnt

# while lt<=rt:
#     mid=(lt+rt)//2
#     if Count(mid)>=c:
#         res = mid
#         lt = mid+1
#     else:
#         rt = mid-1
