import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))
list = [0]
sum=0
for k in num:
  sum += k
  list.append(sum)

for x in range(m):
  i, j = map(int, input().split())
  print(list[j]-list[i-1])