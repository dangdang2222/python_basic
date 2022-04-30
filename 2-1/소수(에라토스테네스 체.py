n = int(input())

count=n
check=0
for i in range(2,n+1):
    for j in range(1,i+1):
        if i%j==0:
            if j!=i and j!=1:
                count-=1
                break
print(count-1)