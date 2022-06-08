import sys
sys.stdin = open("in1.txt","r")

# a = input()
# a = list(a)
# stack = []
# cnt=0
# sum=0
# prev = None

# for x in a:
#     if x==')' : #)
#         if prev ==')':
#             sum+=1
#             if stack:
#                 stack.pop()
#             if cnt!=0:
#                 cnt-=1
#             continue
#         if stack:
#             tmp = stack[-1]
#             if tmp=='(': #()
#                 stack.pop()
#                 sum+=cnt
#                 if cnt!=0:
#                     cnt-=1
#         prev = x
#     else : #(
#         stack.append(x)
#         if len(stack)>1:
#             tmp = stack[-1]
#             if tmp=='(': #((
#                 cnt+=1
#         prev = x
# print(sum)
    
inn = list(input())
stack = []

sum=0
for x in range(len(inn)):
    if inn[x]=='(':
        stack.append('(')
    else: #')'
        if inn[x-1]=='(':
            stack.pop()
            sum+=len(stack)
        else:
            stack.pop()
            sum+=1

print(sum)


