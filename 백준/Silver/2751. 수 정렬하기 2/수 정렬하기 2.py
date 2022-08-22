import sys

n=int(sys.stdin.readline())
number=[]
for i in range(n):
  number.append(int(sys.stdin.readline()))

number = sorted(number)

for i in range(n):
  print(number[i])