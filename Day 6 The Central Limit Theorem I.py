#https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1
#Author- Sajal Agrawal
#sajal.agrawal1997@gmail.com

'''
sample size=49
according to central limit theorem for sample sum(not for sample mean):
new mean for normal dist for sample sum = mean*sample size = 205*49
new std dev for normal dist for sample sum = stddev*sqrt(sample size)
'''
import math 
targetWeight=float(input())
boxes=float(input())
mean=float(input())
stddev=float(input())
newMean=mean*boxes
newStdDev=stddev*math.sqrt(boxes)
ans=0.5*( 1 + math.erf((targetWeight - newMean )/( newStdDev*math.sqrt(2) )) )
print(round(ans,4))