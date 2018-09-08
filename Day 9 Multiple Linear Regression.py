#https://www.hackerrank.com/challenges/s10-multiple-linear-regression/problem
#Author- Sajal Agrawal
#sajal.agrawal1997@gmail.com

import numpy as np
from numpy.linalg import inv
line=input().strip().split(" ")
#print(line)
m=int(line[0]) #no of features 
n=int(line[1]) #no of training examples
x=[]
y=[]
for i in range(n):
    line=input().strip().split(" ")
    #print(line)
    x.append([1.0])
    for j in line[:m]:
        x[i].append(float(j))
    #print(x)
    y.append(float(line[m]))
x=np.array(x)
y=np.array(y)
#print(y.shape)
#print(x)
#print(y)
#xinv=inv(x)
xt=np.transpose(x)
b=inv(xt.dot(x)).dot(xt).dot(y)
#print(b)
q=int(input())
xnew=[]
for i in range(q):
    line=input().strip().split(" ")
    #print(line)
    xnew.append([1.0])
    for j in line[:m]:
        xnew[i].append(float(j))
#print(xnew)
xnew=np.array(xnew)
#print(xnew.dot(b))
for Yi in xnew.dot(b):
    print(round(Yi,2))