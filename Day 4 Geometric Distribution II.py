#https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem
#Author- Sajal Agrawal
#sajal.agrawal1997@gmail.com

x=input().split(" ")
p=float(x[0])/float(x[1])
ins=float(input())
ans=0
for i in range(1,int(ins)+1):
    ans+=( (1-p)**(i-1) ) * p
print(round(ans,3))