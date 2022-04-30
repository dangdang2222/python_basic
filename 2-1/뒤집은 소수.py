n = int(input())
num = list(map(int, input().split()))

def reverse(x):
    count=0
    x_1 = x
    while(1):
        if int(x_1)==0:
            break
        x_1/=10
        count+=1
    length = count
    #print(length)
    max_digit = 1
    for i in range(length-1):
        max_digit*=10
    min_digit=1
    #max_diigt=100
    a=0
    for i in range(length):
        c=int((x/max_digit))
        x-=c*max_digit
        a+=c*min_digit
        min_digit*=10
        max_digit/=10
    return a

def isPrime(x):
    count = 0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    
    if count==2:
        print(x, end=' ')

for i in num:
    result = reverse(i)
    #print(result)
    isPrime(result)
