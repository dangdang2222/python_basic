import sys
sys.stdin = open("in5.txt","r")

n = int(input())
a = list(map(int,input().split()))
max = int(input())
a.sort()
#14, 40, 42, 65, 68, 69, 76, 76, 81, 87

for i in range(max):
    a[0]+=1
    a[n-1]-=1
    a.sort()

print(a[n-1]-a[0])


#hashing으로 해결
L = int(input())
arr = list(map(int,input().split()))
m = int(input())
cnt=[0]*101

maxH = float('-inf')
minH = float('inf')

for x in arr:
    cnt[x]+=1
    if x>maxH : maxH=x
    if x<minH : minH =x

for _ in range(m):
    if cnt[maxH]==1:
        cnt[maxH]-=1
        maxH-=1
        cnt[maxH]+=1
    else:
        cnt[maxH]-=1
        cnt[maxH+1]+=1
    
    if cnt[minH]==1:
        cnt[minH]-=1
        minH+=1
        cnt[minH]+=1
    else:
        cnt[minH]-=1
        cnt[minH+1]+=1

print(maxH-minH)