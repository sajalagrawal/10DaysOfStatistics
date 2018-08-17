#https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem
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
reject=float(x[0])/100
notRej=1-reject
#print("reject %="+str(reject))
#print("not reject %="+str(notRej))
batch=float(x[1])
ans1=0
for i in range(0,3):
    ans1+=nCr(10,i)*(reject**i)*(notRej**(10-i))
print(round(ans1,3))
ans2=0
for i in range(2,11):
    ans2+=nCr(10,i)*(reject**i)*(notRej**(10-i))
print(round(ans2,3))