#https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem
#Author- Sajal Agrawal
#sajal.agrawal1997@gmail.com

import math
def fact(n):
    if(n<=1):
        return 1
    else:
        return n*fact(n-1)
    
lam=float(input())   #lambda=mean
k=int(input()) #k=no of successes
prob=( (lam**k) * (math.exp(-lam)) )/fact(k)
print(round(prob,3))