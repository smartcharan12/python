divd=int(input("enter two numbers="))
d=int(input())

r=divd%d
while(r>0):
    
    divd=d
    d=r
    r=divd%d
print(d)