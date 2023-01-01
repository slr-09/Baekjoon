import sys
input = sys.stdin.readline

n = int(input())
list = []
for i in range(n):
  x,y = map(int,input().split())
  xy = [x,y]
  list.append(xy)

list.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
  print(str(list[i][0])+" "+str(list[i][1]))