import sys
sys.stdin = open("in1.txt","rt")

a = list(range(1,21))

for i in range(10):
    b,c = map(int,input().split())
    
    n = c-b+1
    for k in range(int(n/2)):
        a[b+k-1], a[c-k-1] = a[c-k-1],a[b+k-1]

print(a)

# import sys
# sys.stdin = open("in1.txt","rt")

# a=list(range(21)) #0부터 20까지
# for _ in range(10): #언더바 쓰면 변수 없이
#     s, e= map(int,input().split())

#     for i in range((e-s+1)//2):
#         a[s+i], a[e-i] = a[e-i],a[s+i]