def get(list,s,i):
    if i==s:    
         return 0
    return list[i]+get(list,s,i+1)

a=[]
n=int(input("enter range"))
for i in range (n):
     c=int(input("num"))
     a.append(c)
print(get(a,n,0))
