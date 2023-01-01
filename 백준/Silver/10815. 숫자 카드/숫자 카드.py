import sys
input = sys.stdin.readline

n = int(input())
n_input = set(map(int,input().split()))

m = int(input())
m_input = list(map(int,input().split()))

for i in m_input:
  if i in n_input:
    print(1, end=" ")
  else:
    print(0, end=" ")