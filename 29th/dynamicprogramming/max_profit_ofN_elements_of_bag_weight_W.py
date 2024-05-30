def FindProfit(weight,profit,n,tweight):
    
    if n==0:
     return  0
    if tweight==0:
     return 0
    if weight[n-1>tweight]:
      return FindProfit(weight,profit,n-1,tweight)
    else:
      return max(FindProfit(weight,profit,n-1,tweight),profit[n-1]+FindProfit(weight,profit,n-1,tweight-weight[n-1]))
w=[5,6,1]
tw=6
p=[11,22,3]

n=3
print(FindProfit(w,p,n,tw))
