def pow(x,y):
    if y==0 :
     return 1
    return x*pow(x,y-1)
print(pow(int(input()),int(input())))