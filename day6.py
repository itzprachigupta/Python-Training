print("\tSingle inheritance")
class A:
    def f(self):
        print('A')
class B(A):
    def g(self):
        print('B')
ob=B()
ob.f()
ob.g()
print("****************************************************************************")
print("\tMultilevel inheritance")
class A:
    def f(self):
        print('A')
class B(A):
    def g(self):
        print('B')
class C(B):
    def h(self):
        print('C')
ob=C()
ob.f()
ob.g()
ob.h()
print("****************************************************************************")
print("\tMultiple inheritance")
class A:
    def f(self):
        print('A')
class B():
    def g(self):
        print('B')
class C(A,B):
    def h(self):
        print('C')
ob=C()
ob.f()
ob.g()
ob.h()
print("****************************************************************************")
print("\tHierarchical inheritance")
class A:
    def f(self):
        print('A')
class B(A):
    def g(self):
        print('B')
class C(A):
    def h(self):
        print('C')
ob=C()
ob.f()
ob.h()
print("****************************************************************************")
print("\tHybrid inheritance")
class A:
    def f(self):
        print('A')
class B(A):
    def g(self):
        print('B')
class C(A):
    def h(self):
        print('C')
class D(B,C):
    def i(self):
        print('D')
ob=D()
ob.f()
ob.g()
ob.h()
ob.i()
print("****************************************************************************")
print("\tSuper Keyword")
class student():
	def __init__(self, id, name, Add):
		self.id = id
		self.name = name
		self.Add = Add
class college(student):
	def __init__(self, id, name, Add, roll_no):
		super().__init__(id, name, Add)
		self.roll_no = roll_no

Emp_1 = college(103, "Prachi", "Ludhiana" , 2004641)
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The roll_no is:', Emp_1.roll_no)

print("****************************************************************************")
print("\tPolymorphism")
class A:
    def f(self):
        print("A class")
class B(A):
    def f(self):
        print("B class")
ob=B()
ob.f()
print("****************************************************************************")
print("\tModules")
print("MATH MODULE")
from cmath import sqrt
import math as m
from operator import add, sub
print("Power:",m.pow(2,10))
print("Squareroot:",m.sqrt(25))
print("Factorial:",m.factorial(9))
print("Ceil:",m.ceil(10.9))
print("Floor:",m.floor(10.9))
print("Addition:",add(78,12))
print("Subtraction:",sub(78,12))
print()
print("STRING MODULE")
import string  
for elem in string.ascii_lowercase:
    print(elem,end=' ')
print()
for elem in string.ascii_uppercase:
    print(elem,end=' ')
print()
for elem in string.digits:
    print(elem,end=' ')
print()
for elem in string.punctuation:
    print(elem,end=' ')
print()






