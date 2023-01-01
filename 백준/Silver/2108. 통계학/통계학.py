import sys
input = sys.stdin.readline
from collections import Counter
n = int(input())
sum = 0
list = []
for i in range(n):
  num = int(input())
  list.append(num)
  sum += num
  
list.sort()
max=0
counter = Counter(list).most_common()
max = counter[0][1]
modes=[]
for num in counter:
  if num[1] == max :
    modes.append(num[0])   
modes.sort()
many=0
if(len(modes) == 1):  many = modes[0]
else:  many = modes[1]
if n==1:  many = sum
  
print(round(sum/n))
print(list[int(n/2)])
print(many)
print(list[-1]-list[0])