from re import A
import sys
sys.stdin = open("in1.txt","r")

a = input()
postfix = list(a)

stack=[]
res = 0

for x in postfix:
    if x.isdigit():
        stack.append(x)
    else:
        p2 = int(stack.pop())
        p1 = int(stack.pop())

        if x=='+':
            stack.append(p1+p2)
        elif x=='-':
            stack.append(p1-p2)
        elif x=='/':
            stack.append(p1/p2)
        elif x=='*':
            stack.append(p1*p2)

res = stack.pop()
print(res)