# n = int(input())

# def DFS(n, startnum, step):
#     temp = startnum
#     while True:
#         if temp>n:
#             break
#         else :
#             print(temp, end=' ')
#         temp += step
#     print()

#     step+=1
#     if step>n:
#         return
#     DFS(n, startnum, step)

#     startnum+=1
#     if startnum>n:
#         return
#     DFS(n, startnum,step)
# DFS(3,1,1)

def DFS(m):
    if m==n+1:
        for i in range(1,n+1):
            if list[i]==1:
                print(i, end=' ')
        print()
    else:
        list[m]=1
        DFS(m+1)

        list[m]=0
        DFS(m+1)


if __name__=="__main__":
    n = int(input())
    list = [0]*(n+1)
    DFS(1)