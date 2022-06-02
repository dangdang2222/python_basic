import sys
sys.stdin=open("in5.txt","rt")

n = int(input())
a = [[]*3 for _ in range(n)] # [[0 for _ in range(j)]for _ in range(i)]

for i in range(n):
    a[i] = list(map(int,input().split()))

result_money=[]
for i in a:
    count=0
    eye=0
    if i.count(i[0])==3:
        count=3
        eye=i[0]
    elif i.count(i[0])==2:
        count=2
        eye=i[0]
    else:
        if i.count(i[1])==2:
            count=2
            eye=i[1]
        elif i.count(i[1])==1:
            count=1
            eye=max(i)
    money = 0
    if count==3:
        money = 10000+eye*1000
    elif count==2:
        money = 1000+eye*100
    elif count==1:
        money = eye*100
    result_money.append(money)

print(max(result_money))

# res = 0
# n=int(input())
# for i in range(n):
#     tmp = input().split()
#     tmp.sort()
#     a,b,c=map(int,tmp)

#     if a==b and b==c:
#         money = 10000+a*1000
#     elif a==b or a==c:
#         moeny = 1000 + a*100
#     elif a==b or b==c:
#         money = 1000 + b*100
#     else:
#         money = c*100
#     if money>res:
#         res = moeny
# print(res)