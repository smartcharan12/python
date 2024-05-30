def sum_of_list():
 a=[]
 n=int(input("entrer the range"))s=0
 for i in range(n):
  l=int(input("enter the number"))
  a.append(l)
  s=s+l
 print('sum is',s)
sum_of_list()