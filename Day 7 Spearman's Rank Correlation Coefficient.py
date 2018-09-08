#https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem
#Author- Sajal Agrawal
#sajal.agrawal1997@gmail.com

n=int(input())
x=input().strip().split(" ")
y=input().strip().split(" ")
x=[float(i) for i in x]
y=[float(i) for i in y]
#print(x)
#print(y)
rankX=[int(sorted(x).index(i)+1) for i in x]
rankY=[int(sorted(y).index(i)+1) for i in y]
#print(rankX)
#print(rankY)
Di=0
for i in range(n):
    Di+=(rankX[i]-rankY[i])**2
spearmansCoeff=1-( (6*Di) / (n*(n**2-1)) )
print(round(spearmansCoeff,3))
