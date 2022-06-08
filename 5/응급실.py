import sys
sys.stdin = open("in1.txt","r")
from collections import deque

n, m = map(int,input().split())
a = [(dot, value) for dot, value in enumerate(list(map(int,input().split())))]
a = deque(a)
count=0
while True:
    temp = a.popleft()
    if any(temp[1]<x[1] for x in a ):
        a.append(temp)
    else:
        count+=1
        if temp[0]==m:
            print(count)
            break
