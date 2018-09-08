#https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem
#Author- Sajal Agrawal
#sajal.agrawal1997@gmail.com

x=[]
y=[]
n=5
for i in range(n):
    line=input().strip().split(" ")
    x.append(float(line[0]))
    y.append(float(line[1]))
#print(x)
#print(y))
xsum=0
ysum=0
xysum=0
xsqsum=0
for i in range(len(x)):
    xsum+=x[i]
    xsqsum+=x[i]*x[i]
    ysum+=y[i]
    xysum+=x[i]*y[i]
xmean=xsum/n
ymean=ysum/n
b=(n*xysum-xsum*ysum)/(n*xsqsum-xsum**2)
a=ymean-b*xmean
ans=a+b*80
print(round(ans,3))