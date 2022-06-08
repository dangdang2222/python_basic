import sys
sys.stdin = open("in1.txt","r")

# def DFS(count,n,sum1, sum2):
#     if count==(n):
#         final.append((sum1,sum2))
#         return
    
#     DFS(count+1, n, sum1+a[count], sum2)
#     DFS(count+1,n, sum1,sum2+a[count])


# if __name__ == "__main__":
#     n = int(input())
#     a = list(map(int,input().split()))
#     count=0
#     final=[]
#     DFS(count,n,0,0)

#     if any(x[0]==x[1] for x in final):
#         print("YES")
#     else:
#         print("NO")

def DFS(count, summ):
    if summ>sum(a)//2:
        return
    if count==n:
        if summ==sum(a)//2:
            print("YES")
            sys.exit(0)
    
    
    else: 
        DFS(count+1, summ)
        DFS(count+1, summ+a[count])

if __name__=="__main__":
    n = int(input())
    a=list(map(int,input().split()))

    DFS(0, 0)