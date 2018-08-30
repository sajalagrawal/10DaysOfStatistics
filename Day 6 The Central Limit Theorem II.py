#https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem
#Author- Sajal Agrawal
#sajal.agrawal1997@gmail.com

import math
totalTickets=float(input())
students=float(input())
mean=float(input())
stddev=float(input())
newMean=mean*students
newStddev=stddev*math.sqrt(students)
ans=0.5*( 1 + math.erf( (totalTickets - newMean)/(newStddev*math.sqrt(2)) ) )
print(round(ans,4))