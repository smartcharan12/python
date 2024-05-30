n=int(input())
c=0
for a in range(1,n//2+1):
 if n%a == 0:
  c=c+1
if c>2:
 print("not prime")
else:
 print("prime")