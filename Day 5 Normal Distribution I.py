#https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem
#Author- Sajal Agrawal
#sajal.agrawal1997@gmail.com

import math

line=input().split(" ")
line=[float(i) for i in line]
mean=line[0]
stddev=line[1]
x=float(input())
line=input().split(" ")
line=[float(i) for i in line]
a=line[0]
b=line[1]
px=0.5*(1+ math.erf( (x-mean) / (stddev*math.sqrt(2)) ))
pa=0.5*(1+ math.erf( (a-mean) / (stddev*math.sqrt(2)) ))
pb=0.5*(1+ math.erf( (b-mean) / (stddev*math.sqrt(2)) ))
#print(px,pa,pb)
print(round((px),3))
print(round((pb-pa),3))