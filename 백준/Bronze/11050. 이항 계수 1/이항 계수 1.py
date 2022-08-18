n,k = map(int,input().split())
a=b=1

for i in range(n): a*=i+1
for i in range(k): b*=i+1
if n-k!=0:
  for i in range(n-k): b*=i+1

print(int(a/b))
