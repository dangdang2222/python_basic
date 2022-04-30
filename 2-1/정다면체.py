N,M=map(int,input().split())

sum = []

for i in range(1,N+1):
    for j in range(1,M+1):
        sum.append(i+j)
print(sum)
count = []

for i in range(1, N+M+1):
    count.append(sum.count(i))

print(count)
maximum = max(count)

for index, counts in enumerate(count):
    if counts==maximum:
        print(index+1)