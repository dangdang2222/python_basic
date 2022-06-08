import heapq as hq
import sys

sys.stdin = open("in1.txt","r")

list = []


while True:
    temp = int(input())
    if temp == -1:
        break
    elif temp == 0:
        print(hq.heappop(list))
    else:
        hq.heappush(list,temp)
