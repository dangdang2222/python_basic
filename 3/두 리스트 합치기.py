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