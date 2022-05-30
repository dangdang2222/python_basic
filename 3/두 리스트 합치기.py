import sys
sys.stdin = open("in1.txt","rt")


a_n = int(input())
a = list(map(int,input().split()))
b_n = int(input())
b=list(map(int,input().split()))

a_i=0
b_i=0

c = list()
while(1):
    if a_i == (a_n):
        while(1):
            if b_i == b_n:
                break
            c.append(b[b_i])
            b_i+=1
        break
    elif b_i == (b_n):
        while(1):
            if a_i == a_n:
                break
            c.append(a[a_i])
            a_i+=1
        break
    if a[a_i]>b[b_i]:
        c.append(b[b_i])
        b_i+=1
    else:
        c.append(a[a_i])
        a_i+=1
print(c)

#sort를 쓰면 8log8이 됌
#두 리스트가 이미 정렬되어있다는 사실에 주의하라 --> n으로 해결 가능

# import sys
# sys.stdin = open("in1.txt","r")
# n = int(input())
# a = list(map(int,input().split))
# m = int(input())
# b = list(map(int,input().split))

# p1=p2=0
# c=[]
# while p1<n and p2<m:
#     if a[p1]<=b[p2]:
#         c.append(a[p1])
#         p1+=1
#     else:
#         c.append(b[p2])
#         p2+=1

# if p1<n:
#     c = c+a[p1:]
# if p2<m:
#     c = c+b[p2:]
# for x in c:
#     print(x, end=' ')