import sys
sys.stdin = open("in1.txt","r")


def DFS(L,S):
    global count
    if L==k:
        if sum(res)%m==0:
            count+=1
        # for i in range(0,k):
        #     print(res[i],end=' ')
        # print()
    else:
        for i in range(S,n):
            temp = a[i]
            res[L] = temp
            DFS(L+1,i+1)

if __name__=="__main__":
    n, k = map(int,input().split())
    a=[]
    a = list(map(int,input().split()))
    m = int(input())
    count=0

    res = [0]*k

    DFS(0,0)
    print(count)