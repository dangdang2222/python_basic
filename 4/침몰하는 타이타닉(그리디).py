import sys
sys.stdin = open("in5.txt","r")

n,m = map(int,input().split())
a = list(map(int,input().split()))

a.sort()
cnt=0
while len(a)!=0:
    if len(a)==1:
        cnt+=1
        break
    if a[0]+a[-1]>m:
        cnt+=1
        a.pop(-1)
    else:
        cnt+=1
        a.pop(0)
        a.pop(-1)
    a.sort()

print(cnt)
