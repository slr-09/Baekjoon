n, k = map(int, input().split())
num = []
num = list(map(int, input().split()))
max = 0
sum = 0
for i in range(0,k):
  sum += num[i]  
max=sum

for i in range(0,n-k):
  sum -= num[i]
  sum += num[i+k]
  if sum>max:
    max=sum
    
print(max)