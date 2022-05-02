import sys
sys.stdin = open("in1.txt","rt")

str = input()
num=[]
for i in str:
    if '0'<=i<='9':
        num.append(i)
print(num)

digit=1
for i in range(len(num)-1): #3자리다 그럼 100이 나와야함 0 1 2
    digit*=10
number=0
len = 0
for i in num:
    if len==0:
        if i=='0':
            pass
        else:
            number+=int(((int(i)-int('0'))*digit))
        len+=1
        digit/=10
    else:
        number+=int(((int(i)-int('0'))*digit))
        len+=1
        digit/=10
print(number)
