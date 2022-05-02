import sys
sys.stdin=open("in1.txt","rt")

#수정해야함
N,K=map(int, input().split())
cards = list(map(int, input().split()))
sum=[]

for i in range(N):
    for j in range(i+1,N):
        for r in range(j+1, N):
            sum.append(cards[i]+cards[j]+cards[r])

sum.sort(reverse=True)
print(sum)
count=1
max = -1
for i in range(1,len(sum)):
    if count == K:
        break
    if max != sum[i]:
        count+=1
        max = sum[i]

print(sum[i-1])

'''
import sys
sys.stdin = open("input.txt","rt")
n,k = map(int,input().split())
a = list(map(int, input().split()))
중복을 제거하는 자료구조 set()
res = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1,n):
            res.add(a[i]+a[j]+a[m])

res = list(res)
res.sort(reverse=True)
print(res[k-1])

'''