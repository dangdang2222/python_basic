import sys
sys.stdin = open("in1.txt","r")
from collections import deque

n,k = map(int,input().split())
a = list(map(int,input().split()))
a = deque(a)

max = a.popleft()
a.append(max)

50 70 80 90
for i in range(n):
    