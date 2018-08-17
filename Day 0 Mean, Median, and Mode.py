#https://www.hackerrank.com/challenges/s10-basic-statistics/problem
#Author- Sajal Agrawal
#sajal.agrawal1997@gmail.com

n=int(input())
num=input().split(" ")
num=[int(i) for i in num]
#print(num)
sum=0
for i in num:
    sum=sum+i
mean=sum/n
print(mean)
num=sorted(num)
if(n%2==0):
    median=(num[int(n/2)-1]+num[int(n/2)])/2
else:
    median=num[int(n/2)]
print(median)
map={}
for i in num:
    if (i in map):
        map[i] += 1
    else:
        map[i] = 1    
ans=-1
ansCount=-1
for j in sorted(map):
    #print(j,map[j])
    if(map[j]>ansCount):
        ans=j
        ansCount=map[j]
print(ans)
    