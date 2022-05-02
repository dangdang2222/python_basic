import sys
#sys.stdin=open("in5.txt","rt")

student_num = int(input())
math = list(map(int, input().split()))

average  = sum(math)/len(math)
if average - int(average)>=0.5:
    average = int(average)+1
else:
    average = int(average)

print(average, end=' ')
sub = []
for i in math:
    if i>average:
        sub.append(i-average)
    else:
        sub.append(average-i)

minimal = min(sub)

up = average + minimal
down = average - minimal

result = -1
for index, score in enumerate(math):
    if score == up:
        result = index
        break

if result==-1:
    for index, score in enumerate(math):
        if score == down:
            retult = index
            break

print(result+1)

'''
최솟값 구하기
arr=[5,3,7,9,2,5,2,6]
arrMin = float('inf') //실수 무한대 값
for i in arr:
    if arr[i]<i:
        arrMin=i
'''
'''
import sys
sys.stdin = input("input.txt","rt")
n=int(input())
a=list(map(int,input().split()))

ave=round(sum(a)/n) //소수 첫째자리에서 반올림
min = 2147000000 //정수형 가장 큰 값
for idx, x in enumerate(a):
    tmp = abs(x-ave) //절댓값=거릿값
    if tmp<min:
        min=tmp
        score=x
        res=indx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1
print(ave,res)
'''
'''
round 함수는 round_half_even 방식임
즉 4.50000000 인 경우4가 나옴(정확하게 4.5일때 짝수쪽으로 감)
---> 따라서 반올림,반내림 하려면?
a=66.5
a=a+0.5
a=int(a)
'''


