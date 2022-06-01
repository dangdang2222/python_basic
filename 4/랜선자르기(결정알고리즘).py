#혼자 다시 해보기
#이분 검색을 결정알고리즘에서 사용
#결정 알고리즘 : 찾고자 하는 답의 범위가 정해짐

#모든 랜선을 반드시 사용해야한다라는 조건이 없으므로 가장 긴 랜선의 길이가 최댓값이 됌 
# import sys
# sys.stdin = open("in1.txt", "r")

# def Count(len):
#     cnt=0
#     for x in Line:
#         cnt+=(x//len)
#     return cnt

# k, n =map(int,input().split())
# Line = []
# res = 0
# largest = 0
# for i in range(k):
#     tmp = int(input())
#     Line.append(tmp)
#     largest = max(largest, tmp)

# lt = 1
# rt = largest 
# while lt<=rt:
#     mid = (lt+rt)//2
#     if Count(mid)>=n:
#         res = mid
#         lt = mid+1
#     else:
#         rt = mid-1

# print(res)

import sys
sys.stdin = open("in1.txt","r")

k,n = map(int,input().split())
a=[]
for i in range(k):
    a.append(int(input()))
a.sort()
def cut(n):
    cnt=0
    for i in range(k):
        cnt+=a[i]//n

    return cnt

lt = 1
rt = a[k-1]
res=0
while lt<=rt:
    mid = (lt+rt)//2
    if cut(mid)>=11:
        res = mid
        lt=mid+1
    else:
        rt=mid-1

print(res)
