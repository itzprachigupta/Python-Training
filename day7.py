from operator import index


print("Practice problem 1st")
l1=['m','n']
l2=[]
num=3
for l in (l1):
    for n in range (num):
        z=(l+str(n+1))
        l2.append(z)
print(l2)
print()
print(80*"*")
print("Practice Problem 2nd")
l=[[4,5,3],[6,3,2],[6,9,1]]
l2=[]
sum=0
for item in l:
    for elem in item:
        sum=sum+int(elem)
    l2.append([sum])
    sum=0
print(l2)
print()
print(80*"*")
print("Practice Problem 3rd")
list=[1,2,3,0,1,1,4,5,2,3]
for item in list:
    c=list.count(item)
    if(c>1):
      list.remove(item)
print(list)
print(80*"*")
print("Practice Problem 4th")
for num in range(1200,3000):
    if(num%4==0 and num%8==0 and num%6!=0):
        print(num)



