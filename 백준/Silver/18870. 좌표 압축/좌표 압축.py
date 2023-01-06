import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
copy_set = set()
for i in num:
  copy_set.add(i)
copy_list = list(map(int, copy_set))
copy_list.sort()

copy_dict = {}
for i in range(len(copy_list)):
  copy_dict[copy_list[i]] = i;

for i in num:
  print(copy_dict[i], end=" ")