import sys
sys.stdin = open("in5.txt","r")

n = int(input())
m = [list(map(int,input().split())) for _ in range(n)]

m.sort(key = lambda x : (x[1],x[0]),reverse = True)

h = 0
w = 0
cnt = 0
for height, weight in m:
    if w<weight:
        w = weight
        h = height
        cnt+=1
    elif h<height:
        h = height
        cnt+=1
print(cnt)


# n=int(input())
# body=[]
# for i in range(n):
#     a,b=map(int,input().split())
#     body.append((a,b))
# body.sort(reverse=True)
# largest =0
# cnt=0
# for x,y in body:
#     if y>largest:
#         largest=y
#         cnt+=1