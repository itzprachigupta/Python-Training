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
num=int(input("Enter integer value:"))
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
l=['a','c','d']
print(l)
l.append('e')
print(l)
print(l[2])
print(l[0:4])
l.insert(1,'b')
print(l)
for alp in l:
    print(alp)
print('z' in l)
print('a' in l)
print(len(l))
l.append('f')
print(l)
i=0
while i<len(l):
    print(l[i])
    i+=1
print(l.count('a'))
l.remove('f')
print(l)
l.clear()
print(l)
print("**************************************")
print("Tuple")
t=(1,6,8,4,1,9,3,1)
print(t)
# l.append(88) Not possible in tupple
print(t.count(1))
print(t.index(9))
#t.clear() Not possible in tupple
print("**************************************")
print("Set")
p={1,6,8,4,1,9,3,1}
r={4,8,1}
print(p)
print(r)
q=p.union(r)
print("Union=",q)
q=p.difference(r)
print("Difference=",q)
q=p.symmetric_difference(r)
print("Symmetric Difference=",q)
q=p.intersection(r)
print("Intersection=",q)
print(r.issubset(p))
print(p.isdisjoint(r))
print(f"Length of set p = {len(p)}")
for element in p:
    print(element)
p.remove(3)
print(p)
p.clear()
print(p)
print("**************************************")
print("Frozen set")
p= {1,6,8,4,1,9,3,1}
r={4,8,1}
f=frozenset (p)
g=frozenset (r)
print(f)
print(g)
q=f.union(g)
print("Union=",q)
q=f.difference(g)
print("Difference=",q)
q=f.symmetric_difference(g)
print("Symmetric Difference=",q)
q=f.intersection(g)
print("Intersection=",q)
print(g.issubset(f))
print(f.isdisjoint(g))
print(f"Length of frozen set f = {len(f)}")
for element in f:
    print(element)
print(type(f))
# p.remove(3) Not possible in frozen set
#f.clear() Not possible in frozen set
print("**************************************")
print("Dictionary")
d={'Name':'Prachi','URN':'2004641','Branch':'CSE'}
print(d['Name'])
d['Section']='B'
print(d)
print(d.keys())
print(d.items())
print(f"Length of Dictionary d = {len(d)}")
d['Section']='B2'
print(d)
d.clear()
print(d)
print("**************************************")
print("Function")
def add(a,b):
    c=a+b
    print(c)
add(10,20)
 
