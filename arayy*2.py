a=[[1,2,3,],[4,5,6],[7,8,9]]
a*=2
for i in range (3):
 for j in range (3):
  a[i][j]*=2
for i in range (3):
 for j in range (3):
  print(a[i][j],end=" ")
for i in a:
 print (i)