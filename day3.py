'''Day 3 !!!'''
print("Checking palindrome")
string=input("Enter the string ")
string1= string[::-1]
if(string==string1):
    print("Yes")
else:
    print("No")
    print("Reverse String is ", string1)
print("**************************************")
print("2nd method")
num=int(input("Enter value:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
 print("Palindrome")
else:
 print("Not a Palindrome")
print("**************************************")
print("LIST")
l=["a","b","c"]
print(l)
l.append("d")
print(l)
print("**************************************")
print("Tuple")
t=("A","B","C")
print(t)
print("**************************************")
print("Set")
p={"2","4","7","july"}
r={"10","7","2"}
print(p)
print(r)
q=p.union(r)
print("Union=",q)
q=p.difference(r)
print("Difference=",q)
q=p.intersection(r)
print("Intersection=",q)
print("**************************************")
print("Frozen set")
f=frozenset(p)
print(f)
print(type(f))
print("**************************************")
print("Dictionary")
d={'Name':'Prachi','URN':'2004641'}
print(d)
print("**************************************")
print("Function")
def add(a,b):
    c=a+b
    print(c)
add(10,20)
 
