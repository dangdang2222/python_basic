import sys
sys.stdin = open("in1.txt","r")

n = int(input())
d = dict()

for i in range(n):
    word = input()
    d[word] = 1
for i in range(n-1):
    find = input()
    d[find] = 0
for (keyword, value) in d.items():
    if value==1:
        print(keyword)