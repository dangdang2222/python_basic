import sys
sys.stdin = open("in1.txt","r")


def DFS(L,last):
    global min
    if L==n :
        cnt=0
        for i in range(n):
            cnt+=check[i]
        if cnt<min:
            min = cnt
        return
    else:
        if L==n-1:
            check[L] = last
            DFS(L+1, 0) 

        else:
            iter = last//coins[L]

            for i in range(iter+1):
                check[L] = i
                DFS(L+1, last-i*coins[L])


    

if __name__=="__main__":
    n = int(input())
    coins = list(map(int,input().split()))
    coins.reverse()
    check = [0]*n

    amount = int(input())
    min=float('inf')
    DFS(0,amount)
    print(min)