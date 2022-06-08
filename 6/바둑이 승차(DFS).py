import sys
sys.stdin = open("in1.txt","r")

# def DFS(count,sum,c): 
#     if sum>c :
#         final.append(sum-a[count-1])
#         return
#     if count==5:
#         final.append(sum)
#         return
    
#     DFS(count+1,sum+a[count],c)
#     DFS(count+1,sum,c)

# if __name__=="__main__":
#     c, n = map(int,input().split())
#     a=[]
#     for i in range(n):
#         a.append(int(input()))
#     sum=0
#     count=0
#     final=[]
#     DFS(count,sum,c)
#     print(max(final))
def DFS(count, sum):
    global maxx
    if sum>c:
        return
    if count==n:
        if maxx<sum:
            maxx=sum
    else:
        DFS(count+1, sum+a[count])
        DFS(count+1, sum)

if __name__ == "__main__":
    c, n = map(int,input().split())
    a=[]
    maxx = -1
    for i in range(n):
        a.append(int(input()))
    total = sum(a)

    DFS(0,0)

    print(maxx)