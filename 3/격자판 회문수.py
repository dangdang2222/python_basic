import sys
sys.stdin = open("in1.txt","rt")

a = [[0]*7 for i in range(7)]

for i in range(7):
    a[i] = list(map(int,input().split()))

count=0
for i in range(7):
    for j in range(3):
        if a[i][j] == a[i][j+4]:
            if a[i][j+1] == a[i][j+3]:
                count+=1

for i in range(3):
    for j in range(7):      
        if a[i][j] == a[i+4][j]:
            if a[i+1][j] == a[i+3][j]:
                count+=1

print(count)