print("Encapsulation")
print("PROTECTED MEMBER")
class parent:
    def __init__(self):
        self._a=10
class child(parent):
    def __init__(self):
        parent.__init__(self)
        print("Protected member:",self._a)
        self._a=15
        print("Modified protected member:",self._a)
ob1=parent()
ob2=child()
print("Protected member of ob1:",ob1._a)
print("Protected member of ob2:",ob2._a)
print(80*"*")
p="private member"
print(p.upper())
class parent:
    def __init__(self):
        self.a=10
        self._b=20
        self.__c=30
        print("Private member:",self.__c)
class child(parent):
    def __init__(self):
        parent.__init__(self) 
        print("Publlic member:",self.a)
        print("Protected member:",self._b)
       #print("Private member:",self.__c)
        self.a=15
        self._b=25
        self.__c=35
        print("Modified public member:",self.a)
        print("Modified protected member:",self._b)
        print("Modified private member:",self.__c)
ob1=parent()
ob2=child()
print("Public member of ob1:",ob1.a)
print("Public member of ob2:",ob2.a)
print("Protected member of ob1:",ob1._b)
print("Protected member of ob2:",ob2._b)
#print("Private member of ob1:",ob1.__c)
#print("Private member of ob2:",ob2.__c)
print(80*"*")
print("ABSTRACTION")
from abc import ABC,abstractmethod
class language(ABC):
    @abstractmethod
    def region(self):
        pass
class punjabi(language):
    def region(self):
        print("Punjabi is Punjab's language")
class gujrati(language):
    def region(self):
        print("Gujrati is Gujrat's language")
class marathi(language):
    def region(self):
        print("Mararthi is Maharastra's language")
class odiya(language):
    def region(self):
        print("Odiya is Odissa's language")
class harayanvi(language):
    def region(self):
        print("Harayanvi is Harayana's language")
z=punjabi()
z.region()
z=gujrati()
z.region()
z=marathi()
z.region()
z=odiya()
z.region()
z=harayanvi()
z.region()
print(80*"*")
print("EXCEPTION HANDLING 1")
a=[8,9,5,3,22,10,77]
try:
    print("3rd element:",a[2])
    print("8th element:%d" %(a[7]))
except:
    print("Index Out of bound")
print("EXCEPTION HANDLING 2")
def div(a,b):
    try:
        c=((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
div(10,5)
div(5,5)
