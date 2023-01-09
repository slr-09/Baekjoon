import sys
input = sys.stdin.readline

n,m = map(int,input().split())
n_dict={}
for i in range(n):
  n_dict[input().strip()] = i+1 

reverse_dict = dict(map(reversed, n_dict.items()))
for i in range(m):
  m_input = input()
  m_input = m_input.replace("\n","")
  if m_input.isdigit():
    print(reverse_dict[int(m_input)])
  elif not m_input.isdigit():
    print(n_dict[m_input])

