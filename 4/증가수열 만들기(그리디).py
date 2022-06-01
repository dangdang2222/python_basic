import sys
sys.stdin = open("in1.txt","r")

n = int(input())
a = list(map(int,input().split()))
list = []

tmp=0
cnt=0
# while len(a)!=0:
#     if a[0]<=a[-1]:
#         if a[0]>tmp:
#             tmp=a[0]
#             list.append('L')
#             a.pop(0)
#             cnt+=1
#             if len(a)==1:
#                 break
#     else :#a[0]>a[-1]
#         if a[-1]>tmp:
#             tmp = a[-1]
#             list.append('R')
#             a.pop(-1)
#             cnt+=1
# print(cnt + list)
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