import sys
sys.stdin = open("in1.txt","rt")

a = list(range(1,21))

for i in range(10):
    b,c = map(int,input().split())
    
    n = c-b+1
    for k in range(int(n/2)):
        a[b+k-1], a[c-k-1] = a[c-k-1],a[b+k-1]

print(a)