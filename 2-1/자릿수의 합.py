import sys
#sys.stdin=open("in5.txt","rt")

N = int(input())
num = list(map(int,input().split()))
def digit_sum(x):
    sum=0
    na =0
    digit=10

    while(1):
        if x==0:
            break
        na = x%digit
        sum+=na
        x/=digit
        x = int(x)

    return sum

sum=[]
for i in num:
    sum.append(digit_sum(i))

for i in range(N+1):
    if sum[i] == max(sum):
        print(num[i])
        break

# import sys
# sys.stdin=open("in5.txt","rt")

# n = int(input())
# a=list(map(int,input().split()))

# def digit_sum(x):
#     sum=0
#     while x>0:
#         sum+=x%10
#         x=x//10
#     return sum

# max=-2147000000
# for x in a:
#     tot = digit_sum(x)
#     if tot>max:
#         max=tot
#         res = x


# gg
