#https://www.hackerrank.com/challenges/s10-standard-deviation/problem
#Author- Sajal Agrawal
#sajal.agrawal1997@gmail.com

n=int(input())
num=input().split(" ")
num=[int(i) for i in num]
sum=0
mean=0
for i in num:
    mean+=i
mean=mean/n
for i in num:
    sum+=(i-mean)**2
#print("sum="+str(sum))
variance=sum/n
#print("var="+str(variance))
stddev=variance**(1/2)
print(round(stddev,1))