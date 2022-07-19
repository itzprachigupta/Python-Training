'''Day 2'''
a=8
b=4
c=2
print("Arithmetic", a+b, a-b, a*b, a/b, a//b, a%b, a**b)
print("Relational", a>b, a<b, a>=b, a<=b, a==b, a!=b)
print("logical", a>b and b>c, a>b or b>c, not(a>b and b>c))
print("Bitwise", a&b, a|b, a^b, ~a, ~b, ~c)
a+=2 
b+=7
print("Assignment", a, b)
if(a>b):
    print("Condition", a)
else:
    print("Condition", b)
print("Looping")
print("Pattern 1")
for x in range (4):
   for y in range(4):
     print('*',end='')
   print()
print("Pattern 2")
x=5
for x in range(1,x+1):
   for y in range (1,x+1):
     print("*", end='')
   print()
print("Pattern 3")
x=5
for x in range(1,x+1):
   for y in range (1,x+1):
     print(x, end='')
   print()
print("while loop")
z=1;
while(z<=10):
    print(2*z)
    z+=1
print("jumping")
for z in range(15):
  if(z%2==0):
     continue
  elif(z==15):
     break
  print(z)

