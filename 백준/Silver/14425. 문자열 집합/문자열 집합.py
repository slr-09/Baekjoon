import sys
input = sys.stdin.readline

n, m = map(int,input().split())
n_map = set()
m_list = []
for i in range(n):
  n_input = input()
  n_map.add(n_input)
for i in range(m):
  m_input = input()
  m_list.append(m_input)

count=0
for i in m_list:
  if i in n_map:
    count += 1

print(count)