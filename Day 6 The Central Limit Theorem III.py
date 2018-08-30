#https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem
#Author- Sajal Agrawal
#sajal.agrawal1997@gmail.com

'''
values for actual population:
mean=500
std dev=80
sample size=100

sample mean distribution by central limit theorem:
mean=population mean=500
sample stddev=80/sqrt(100)=8
middle 95% of distribution is at distance 2*standardDeviation from both sides of mean

if you read the question carefully, you will notice he tells you the poulation mean and population standard deviation but asks you for the interval on the sample.
'''
import math
sampleSize=float(input())
populationMean=float(input())
populationStdDev=float(input())
interval=float(input())
zScore=float(input())
sampleMean=populationMean
sampleStdDev=populationStdDev/math.sqrt(sampleSize)
print(round(sampleMean - zScore*sampleStdDev,3))
print(round(sampleMean + zScore*sampleStdDev,3)) 