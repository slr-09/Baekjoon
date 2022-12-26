import sys
input = sys.stdin.readline
k = int(input())
list = []
for i in range(k):
  x = int(input())
  if x==0:
    list.pop()
  else:
    list.append(x)
    
sum=0
for num in list:
  sum += num

print(sum)