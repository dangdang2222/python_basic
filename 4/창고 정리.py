import sys
sys.stdin = open("in5.txt","r")

n = int(input())
a = list(map(int,input().split()))
max = int(input())
a.sort()
#14, 40, 42, 65, 68, 69, 76, 76, 81, 87

for i in range(max):
    a[0]+=1
    a[n-1]-=1
    a.sort()

print(a[n-1]-a[0])