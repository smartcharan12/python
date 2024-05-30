a=[]
n=int(input("enter  the no of numbers"))
for i in range(n):
 p=int(input("enter the number"))
 a.append(p)
x=int(input("enter number to search"))

def numsearch(x,list,size):
 for i in range(size):
  if list[i]==x:
    return True
 print("false")
 

print(numsearch(x,a,n))