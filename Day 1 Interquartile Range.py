#https://www.hackerrank.com/challenges/s10-interquartile-range/problem
#Author- Sajal Agrawal
#sajal.agrawal1997@gmail.com

def median(list):
    n=len(list)
    #print(list)
    #print(n)
    if(n%2==0):
        median=(list[int(n/2)-1]+list[int(n/2)])/2
    else:
        median=list[int(n/2)]
    return median

n=int(input())
num=input().split(" ")
num=[int(i) for i in num]
freq=input().split(" ")
freq=[int(i) for i in freq]
list=[num[i] for i in range(len(freq)) for j in range(freq[i])]
list=sorted(list)
#print(list)
n=len(list) #length of new list
if(len(list)%2==0):
    q1=median( list[:int(n/2)] ) #second index in splice is not included
    q3=median( list[int(n/2):] )
else:
    q1=median( list[:int(n/2)] )   #second index in splice is not included
    q3=median( list[int(n/2)+1:] )
q2=median(list)
#print(int(q1))
#print(int(q2))
#print(int(q3))
print(round(float(q3-q1),1))