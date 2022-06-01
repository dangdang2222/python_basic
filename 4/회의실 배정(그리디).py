import sys
sys.stdin = open("in1.txt","r")
#그리디는 거의 정렬이다
#현재 문제는 빨ㄹ ㅣ끝나는게 중요해서 끝나는 시간으로 정렬함

n = int(input())
meeting = []
for i in range(n):
    s,e =map(int,input().split())
    meeting.append((s,e)) #튜플

meeting.sort(key=lambda x : (x[1],x[0]))
et = 0
cnt = 0
for s, e in meeting:
    if s>=et:
        et = e
        cnt+=1
print(cnt)