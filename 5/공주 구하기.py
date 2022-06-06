import sys
from collections import deque


sys.stdin = open("in1.txt","rt")

n,k = map(int,input().split())
q = deque()

for i in range(1,n+1):
    q.append(i)

current=0
while len(q)!=1:
    for _ in range(k-1):
        temp = q.popleft()
        q.append(temp)
    q.popleft()
    
print(q.pop())
