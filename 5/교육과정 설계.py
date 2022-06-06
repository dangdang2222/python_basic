import sys
sys.stdin = open("in2.txt","r")

ess = list(input())
n = int(input())

for i in range(n):
    check = list(input())
    current = -1 #0부터 len(ess)까지
    probnext = 1
        
    for k in check:
        flag = 0
        for j in range(len(ess)): #CBA 중 C부터 체크:
            if k ==ess[j]:
                flag = 1
                break
        if flag==1:
            if j==0:
                current = 0
            if j!=current: 
                if j==probnext:
                    if current!=-1:
                        current = probnext
                        probnext +=1
                    else:
                        print("#%d NO" %(i+1))
                        break
                else:
                    print("#%d NO" %(i+1))
                    break
            if current == len(ess)-1:
                print("#%d YES" %(i+1))
                break
        else:
            if k==check[-1]:
                print("#%d NO" %(i+1))
                break
