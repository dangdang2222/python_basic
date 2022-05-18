import sys
sys.stdin = open("in1.txt","rt")

N, M = map(int, input().split())

a = list(map(int,input().split()))

count=0
add=0
for i in range(0,N):
    for j in range(i, N):
        if i==j:
            add += a[j]
            if add<M:
                continue
            elif add==M:
                count+=1
                add=0
                break
            else :
                add=0
                break

        else:
            add += a[j]
            if add<M:
                continue
            elif add==M:
                count+=1
                add=0
                break
            else :
                add=0
                break

print(count)