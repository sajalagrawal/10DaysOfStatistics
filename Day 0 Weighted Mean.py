#https://www.hackerrank.com/challenges/s10-weighted-mean/problem
#Author- Sajal Agrawal
#sajal.agrawal1997@gmail.com

n=int(input())
x=input().split(" ")
w=input().split(" ")
x=[int(i) for i in x]
w=[int(i) for i in w]
sum=0;
totalWeight=0
for i in range(n):
    sum=sum+x[i]*w[i]
    totalWeight=totalWeight+w[i]
weightedMean=sum/totalWeight
print(round(weightedMean,1)) #imp to round off 