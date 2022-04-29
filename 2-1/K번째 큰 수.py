N,K=map(int, input().split())
cards = list(map(int, input().split()))
sum=[]

for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for r in range(j+1, len(cards)):
            sum.append(cards[i]+cards[j]+cards[r])

sum.sort(reverse=True)
print(sum[K-1])