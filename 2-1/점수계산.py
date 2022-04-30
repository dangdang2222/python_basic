import sys
sys.stdin=open("in5.txt","rt")

n = int(input())
ex=  list(map(int, input().split()))

extra=0
plus=0
sum=0
for i in ex:
    if i==1:
        sum+=1
        sum+=extra
        extra+=1
    else: #i==0
        sum+=0
        extra=0

print(sum)