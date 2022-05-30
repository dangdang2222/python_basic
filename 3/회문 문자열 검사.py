import sys
sys.stdin = open("in1.txt","rt")

n = int(input())
for i in range(n):
    s = input()
    s=s.lower()
    for j in range(int(len(s)/2)): #01234 (5) 012345(6)
        if s[j]!=s[len(s)-j-1]:
            print('#%d NO' %(i+1))
            break
    else:
        print('#%d YES'%(i+1))


# import sys
# sys.stdin = open("in1.txt","rt")

# n = int(input())
# for i in range(n):
#     s = input()
#     s = s.upper()
#     size=len(s)
#     for j in range(size//2):
#         if s[j]!=s[-(j+1)]:
#             print("#%d NO" %(i+1))
#             break
#     else:
#        print("#%d YES" %(i+1))

# import sys
# sys.stdin = open("in1.txt","rt")

# n = int(input())
# for i in range(n):
#     s = input()
#     s = s.upper()
#     if s==s[::-1]:
#          print("#%d YES" %(i+1))


