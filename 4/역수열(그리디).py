import sys
sys.stdin = open("in5.txt","r")

n = int(input())
a = list(map(int,input().split()))
a = a[::-1]
print(a)
list=[]
for i in range(n):
    number = n-i
    big = a[i]

    cnt=0
    if big==0:
        list.insert(0,number)
        continue
    for j in list:
        if j>number:
            cnt+=1
        if cnt==big:
            list.insert(cnt,number)
            break

print(list)
