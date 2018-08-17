#https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem
#Author- Sajal Agrawal
#sajal.agrawal1997@gmail.com

def fact(n):
    if(n<=1):
        return 1
    else:
        return n*fact(n-1)
    
def nCr(n,r):
    return fact(n)/(fact(n-r)*fact(r))

x=input().split(" ")
b=float(x[0])
g=float(x[1])
success=b/(b+g)
failure=1-success
ans=0
#print("b="+str(b))
#print("g="+str(g))
#print("success="+str(success))
#print("failure="+str(failure))
for i in range(3,7):
    #print(ans)
    ans=ans + nCr(6,i)*(success**i)*(failure**(6-i))
print(round(ans,3))