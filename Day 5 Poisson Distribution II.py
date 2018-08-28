#https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem
#Author- Sajal Agrawal
#sajal.agrawal1997@gmail.com

line=input().split(" ")
line=[float(i) for i in line]
lamA=float(line[0])     #expectation of X, E[X]=lamA
lamB=float(line[1])     #expectation of Y, E[Y]=lamB
expX2=lamA+lamA**2      #expX2 is E[X^2]
expY2=lamB+lamB**2      #expY2 is E[Y^2]
ansA=160+40*(expX2)     
ansB=128+40*(expY2)      
print(round(ansA,3))
print(round(ansB,3))