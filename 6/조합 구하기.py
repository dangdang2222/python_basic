from re import M


def DFS(L,S):
    global count
    if L==m+1 :
        count+=1
        for i in range(1,m+1):
            print(res[i],end=' ')
        print()
    else:
        for i in range(S,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1,i+1)
                ch[i]=0


if __name__ == "__main__":
    n, m = map(int,input().split())
    res = [0]*(M+1)
    ch = [0]*(n+1)
    count=0
    DFS(1,1)
    print(count)