import sys
input = sys.stdin.readline

n = int(input())
list = []
n = str(n)
for i in range(0,len(n)):
  list.append(n[i])
list.sort(reverse=True)

for i in range(len(n)):
  print(list[i], end="")