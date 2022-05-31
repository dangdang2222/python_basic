import sys
sys.stdin = open("in1.txt","rt")

a = [[0]*7 for i in range(7)]

for i in range(7):
    a[i] = list(map(int,input().split()))

count=0
for i in range(7):
    for j in range(3):
        if a[i][j] == a[i][j+4]:
            if a[i][j+1] == a[i][j+3]:
                count+=1

for i in range(3):
    for j in range(7):      
        if a[i][j] == a[i+4][j]:
            if a[i+1][j] == a[i+3][j]:
                count+=1

print(count)


# board = [list(map(int,input().split())) for _ in range(7)]
# cnt=0

# for i in range(3):
#     for j in range(7):
#         tmp = board[j][i:i+5]
#         if tmp==tmp[::-1] :#회문은 [::-1]로 하면 됌
#             cnt+=1
        
#         for k in range(2):
#             if board[i+k][j]!=board[i+5-k-1][j]:
#                 break
#         else:
#             cnt+=1
    