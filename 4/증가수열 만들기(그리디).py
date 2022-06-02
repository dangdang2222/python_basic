import sys
sys.stdin = open("in1.txt","r")

n = int(input())
a = list(map(int,input().split()))
list = []

tmp=0
cnt=0
while len(a)!=0:
    if a[0]>tmp and a[-1]>tmp:
        if a[0]<=a[-1]:
            tmp=a[0]
            list.append('L')
            a.pop(0)
            cnt+=1
        else :#a[0]>a[-1]
            tmp = a[-1]
            list.append('R')
            a.pop(-1)
            cnt+=1
    elif a[0]>tmp:
        tmp = a[0]
        list.append('L')
        a.pop(0)
        cnt+=1
    elif a[-1]>tmp:
        tmp = a[-1]
        list.append('R')
        a.pop(-1)
        cnt+=1
    else:
        break
print(cnt)
for i in list:
    print(i, end=' ')


#내 코드는 pop이 너무 많아서 비효율적임 
#이럴때는 index를 가르키는 포인터처럼 쓰는게 편함

# n=int(input())
# a = list(map(int,input().split()))

# lt=0
# rt=n-1
# last =0
# res = ""
# tmp=[]

# while lt<=rt:
#     if a[lt]>last:
#         tmp.append((a[lt],'L'))
#     if a[rt]>last:
#         tmp.append((a[rt],'R'))
#     tmp.sort()

#     if len(tmp)==0:
#         break
#     else:
#         res = res + tmp[0][1]
#         last = tmp[0][0]
#         if tmp[0][1]=='L':
#             lt+=1
#         else:
#             rt+=1
#     tmp.clear()
