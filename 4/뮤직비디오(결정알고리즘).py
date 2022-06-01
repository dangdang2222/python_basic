import contextlib
import sys
from turtle import Turtle
sys.stdin = open("in5.txt","r")

n,m = map(int,input().split())
songs = list(map(int,input().split()))

total = sum(songs)
lt = 1
rt = total

def check(n,m,k):
    sum=0
    cnt=0
    i=0
    while i<n:
        sum+=songs[i]
        if sum>k:
            sum=0
            cnt+=1
            i-=1
        elif sum==k:
            sum=0
            cnt+=1
        i+=1
    if sum<k and sum!=0:
        cnt+=1
    #print(k, cnt)
    if cnt<=m:
        return True
    else:
        return False
    
res=0
while lt<=rt:
    mid = (lt+rt)//2
    #mid=17
    if check(n,m,mid)==True:
        res= mid
        rt = mid-1
    else:
        lt=mid+1


print(res)
        