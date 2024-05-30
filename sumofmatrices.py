x=int(input("rows"))
y=int(input("cols"))
a1=[[0 for _ in range (x)] for _ in range (y)]
a2=[[0 for _ in range (x)] for _ in range (y)]
 
for i in range (x):
 for j in range (y):
  a1[i][j]=int(input())
print("a2")
for i in range (x):
 for j in range (y):
  a2[i][j]=int(input())
  a1[i][j]=a1[i][j]+a2[i][j]
print("sum of matrix")
for i in range (x):
 for j in range (y):
  print(a1[i][j],end=" ")
 print("")
