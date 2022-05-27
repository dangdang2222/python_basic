import sys
sys.stdin = open("in1.txt","rt")

a = [[0]*9 for i in range(9)]
for i in range(9):
    a[i] = list(map(int,input().split()))

for i in range(9):
    for k in range(9):
        for p in range(k+1,9):
            if a[i][k] == a[i][p] :
                print("NO")
                exit()
            

for i in range(9):
    for k in range(9):
        for p in range(k+1,9):
            if a[k][i] == a[p][i] :
                print("NO")
                exit()

for i in range(3):
    for k in range(3):
        for p in range(3):
            for w in range(3):
                for e in range(3):
                    if k==w and p==e:
                        continue
                    if a[i*3+k][i*3+p] == a[i*3+w][i*3+e]:
                        print("NO")
                        exit()

print("YES")

            
