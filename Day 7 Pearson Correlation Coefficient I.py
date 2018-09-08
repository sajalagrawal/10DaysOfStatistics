#https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem
#Author- Sajal Agrawal
#sajal.agrawal1997@gmail.com

import math
n=int(input())
line=input().strip().split(" ")
x=[float(i) for i in line]
line=input().strip().split(" ")
y=[float(i) for i in line]
sumX=0
sumY=0
for i in range(n):
    sumX+=x[i]
    sumY+=y[i]
meanX=sumX/n
meanY=sumY/n
#print(meanX)
#print(meanY)
sumOfSquaresX=0
sumOfSquaresY=0
for i in range(n):
    sumOfSquaresX+=(x[i]-meanX)**2
    sumOfSquaresY+=(y[i]-meanY)**2
stddevX=math.sqrt(sumOfSquaresX/n)
stddevY=math.sqrt(sumOfSquaresY/n)
#print(stddevX)
#print(stddevY)
correlation=0
for i in range(n):
    correlation+=(x[i]-meanX)*(y[i]-meanY)
correlation=correlation/(n*stddevX*stddevY)
print(round(correlation,3))