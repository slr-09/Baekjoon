import sys
input = sys.stdin.readline

n,m = map(int,input().split())
n_set = set()
m_set = set()

for i in range(n):
  n_set.add(input())

for i in range(m):
  m_set.add(input())

sett = sorted(list(set(n_set&m_set)))
print(len(n_set & m_set))
for i in sett:
  print(i,end="")