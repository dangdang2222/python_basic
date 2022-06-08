import sys
sys.stdin = open("in1.txt","r")

# infix = input()
# infix = list(infix)

# postfix=[]
# stack=[]

# for x in infix:
#     if x.isdigit():
#         postfix.append(x)
#     else:
#         if stack:
#             tmp = stack[-1]
#             if x=='(' or x==')':
#                 if x==')':
#                     while True:
#                         ttmp = stack.pop()
#                         if ttmp=='(':
#                             break
#                         else:
#                             postfix.append(ttmp)
#             elif x=='*' or x=='/':
#                 if tmp=='*' or tmp=='/':
#                     postfix.append(stack.pop())
#             elif x=='+' or x=='-':
#                 if tmp=='*' or tmp == '/':
#                     postfix.append(stack.pop())
#                     if stack:
#                         if stack[-1]=='+' or stack[-1]=='-':
#                             postfix.append(stack.pop())
#                 elif tmp=='+' or tmp=='-':
#                     postfix.append(stack.pop())
#         if x!=')':
#             stack.append(x)
# while stack:
#     postfix.append(stack.pop())

# res = ''.join(map(str,postfix))
# print(res)

inn = list(input())
stack=[]
str = []

for x in inn:
    if x.isdigit():
        str.append(x)
    elif x == '(':
        stack.append('(')
    elif x=='*' or x=='/':
        while stack and (stack[-1]=='*' or stack[-1]=='/'):
            str.append(stack.pop())
        stack.append(x)
    elif x=='+' or x=='-':
        while stack and (stack[-1]=='-' or stack[-1]=='+' or stack[-1]=='*' or stack[-1] =='/'):
            str.append(stack.pop())
        stack.append(x)
    elif x==')':
        while stack and stack[-1]!='(':
            str.append(stack.pop())
        stack.pop()

while stack:
    str.append(stack.pop())

print(''.join(str))

