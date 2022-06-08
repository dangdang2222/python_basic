import sys
sys.stdin = open("in1.txt","r")

n = int(input())
st = []
def div(n):
    if n==0:
       return st
    st.append(n%2)
    div(n//2)
div(n)
st.reverse()
at = ''.join(map(str,st))
print(at)