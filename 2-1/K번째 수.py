import sys
#sys.stdin=open("in5.txt","rt")

case_num = int(input())
result = []
for i in range(case_num):
    N, s,e,k = map(int, input().split(' '))
    a= []
    a= list(map(int, input().split()))
    b = a[s-1:e]
    b.sort()
    result.append(b[k-1])

for i in range(case_num):
    print('#',(i+1),' ',result[i])