#https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem
#Author- Sajal Agrawal
#sajal.agrawal1997@gmail.com

import math

line=input().split(" ")
line=[float(i) for i in line]
mean=line[0]
stddev=line[1]
a=float(input())
b=float(input())
p80=0.5*(1+ math.erf((80-mean)/(stddev*math.sqrt(2))) ) #cumulative probability for percentage<=80
p60=0.5*(1+ math.erf((60-mean)/(stddev*math.sqrt(2))) ) #cumulative probability for percentage<=60
print(round((1-p80)*100,2))
print(round((1-p60)*100,2))
print(round(p60*100,2))