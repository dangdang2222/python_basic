import sys
sys.stdin = open("in5.txt","r")

n,m = map(int,input().split())
a = list(map(int,input().split()))

a.sort()
cnt=0
while len(a)!=0: #그냥 while a로 해도 됌
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

#list에서 pop(0)을 하면 맨 앞에거를 빼고 나머지를 한칸씩 땡김
#상당히 비효율적
#따라서 deque를 사용함

import sys
from collections import deque
sys.stdin = open("input.txt","r")
n, limit = map(int,input().split())
a=list(map(int,input().split()))
a.sort()
a=deque(a)
cnt = 0

while len(a)!=0: #그냥 while a로 해도 됌
    if len(a)==1:
        cnt+=1
        break
    if a[0]+a[-1]>m:
        cnt+=1
        a.pop() #default가 맨 뒤에서 빼는거임
    else:
        cnt+=1
        a.pop()
        a.popleft() #pop(0) 즉 맨 앞에서 빼는것과 동일
    a.sort()

print(cnt)