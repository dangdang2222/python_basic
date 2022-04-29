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




