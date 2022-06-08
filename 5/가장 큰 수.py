import sys
sys.stdin = open("in1.txt","r")

number, n = map(int,input().split())
number = list(map(int,str(number)))

stack = []
count=0
for x in number:
    while stack and stack[-1]<x and count<n:
        count+=1
        stack.pop()
    
    stack.append(x)

while count<n:
    count+=1
    stack.pop()

print(''.join(map(str,stack)))