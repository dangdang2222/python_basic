import sys
#sys.stdin=open("in5.txt","rt")

N,M=map(int,input().split())

sum = []

for i in range(1,N+1):
    for j in range(1,M+1):
        sum.append(i+j)
count = []

for i in range(1, N+M+1):
    count.append(sum.count(i))

maximum = max(count)

for index, counts in enumerate(count):
    if counts==maximum:
        print(index+1, end=' ')

'''
import sys
sys.stdin = input("input.txt","rt")
n,m= map(int,input().split)
cnt = [0]*(n+m)

for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1
max=-2147000000
for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]

for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=' ')
'''