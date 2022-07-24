print("\tGlobal Variables")
x = 5
def f():
    x = 10
    print("local x:", x)
f()
print("global x:", x)
print("****************************************************************************")
print("\tClass")
class animal:
    def mammal(self):
        print("Dog is a mammal")
        def fun():
            print("Dog has four legs")
        fun()
ob=animal()
ob.mammal()
print("****************************************************************************")
print("\tConstructor")
class Addition:
	first = 0
	second = 0
	answer = 0
	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s
	
	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second
obj = Addition(10, 40)
obj.calculate()
obj.display()
print("****************************************************************************")
print("\tDestructor")
class Employee:
	def __init__(self):
		print('Employee created.')
	def __del__(self):
		print('Destructor called, Employee deleted.')
obj = Employee()
del obj

