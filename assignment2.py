'''Assignment 2'''
print("Answer 1")
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
num=int(input("Enter number:"))
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
print("Answer 2")
fact=1
n=input("Enter any number:")
n=int(n)
for x in range (1,n+1):
    fact=fact*x
print("Factorial of ",n,":",fact)
print("**************************************")
print("Answer 3")
nterms = int(input("Enter number of terms:"))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
print("**************************************")
print("Answer 4")
num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
print("**************************************")
print("Answer 5")
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break   
    else:
        print("Invalid Input")
print("**************************************")
print("Answer 6")
print("Pattern 1")
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")
print("Pattern 2")
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")
print("Pattern 3")
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")   
    print("\n")
print("Pattern 4")
rows = int(input("Enter number of rows: "))
k = 0
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1   
    k = 0
    print()
print("**************************************")
print("Answer 7")
year=input("Enter a year: ")
year=int(year)
if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print(year," is a leap year.")
else: 
   print(year," is not a leap year.")
print("**************************************")
print("Answer 8")
num = int(input("Enter a number: "))
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")
print("**************************************")
print("Answer 9")
def calculate_area(name):
  if name =='1':
    l = int(input("Enter rectangle's length: "))
    b = int(input("Enter rectangle's breadth: "))  
    rect_area = l * b
    print("The area of rectangle is ",rect_area)  
  elif name == '2':
    s = int(input("Enter square's side length: "))
    sqt_area = s * s
    print("The area of square is",sqt_area) 
  elif name == '3':
    h = int(input("Enter triangle's height length: "))
    b = int(input("Enter triangle's breadth length: "))
    tri_area = 0.5 * b * h
    print("The area of triangle is ",tri_area)
  elif name == '4':
    r = int(input("Enter circle's radius length: "))
    pi = 3.14
    circ_area = pi * r * r
    print("The area of circle is",circ_area)
  else:
    print("Sorry! This shape is not available")
print("Calculate Shape Area")
print("Enter the name of shape whose area you want to find: ")
shape = input("1:Rectangle\n2:Square\n3:Triangle\n4:Circle")
calculate_area(shape)
print("**************************************")
print("Answer 10")
lst = [7,52,6,94,1,12]
lst.reverse()
print("Reversed List:", lst)
print("**************************************")
print("Answer 11")
total = 0
list1 = [11, 5, 17, 18, 23]
for ele in range(0, len(list1)):
    total = total + list1[ele]
print("Sum of all elements in given list: ", total)
print("**************************************")
print("Answer 12")
somelist =  [1,12,2,53,23,6,17] 
max_value = max(somelist)
print("Maximum=",max_value)
min_value = min(somelist)
print("Minimum=",min_value)
if len(somelist) == 0:
    avg_value = 0
    print("Average=",avg_value)
else:
    avg_value=sum(somelist)/len(somelist)
    print("Average=",avg_value)
print("**************************************")
print("Answer 13")
def grouping_dictionary(l):
    result = {}
    for k, v in l:
         result.setdefault(k, []).append(v)
    return result
colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print("Original list:")
print(colors)
print("\nGrouping a sequence of key-value pairs into a dictionary of lists:")
print(grouping_dictionary(colors))

def nested_dictionary(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result
print("**************************************")
print("Answer 14")
student_id = ["1", "2", "3", "4"] 
student_name = ["Alisha", "Laila", "Danish", "Sam"] 
student_grade = [25,35,26,45]
print("Original strings:")
print(student_id)
print(student_name)
print(student_grade)
print("\nNested dictionary:")
ch='a'
print(nested_dictionary(student_id, student_name, student_grade))
print("**************************************")
print("Answer 15")
setA={89,76,55,4,32,1}
setB={89,1,32}
setC= setA.intersection(setB)
print("Set A=",setA)
print("Set B=",setB)
print("A intersection B=",setC)
if(setC==setB):
    print("Set B is a subset of set A")
else:
    print("Set B is not a subset of set A")
print("**************************************")
print("Answer 16")
setA={1,3,6,8,9}
setB={3,7,11,4,6}
symdiff= setA.symmetric_difference(setB)
setdiff=setA.difference(setB)
print("Set A=",setA)
print("Set B=",setB)
print("Symmetric Difference A^B=",symdiff)
print("Symmetric Difference A-B=",setdiff)
print("**************************************")
print("Answer 17")
def Remove(tuples):
    for i in tuples:
        if(len(i)==0):
            tuples.remove(i)
    return tuples
tuples = [(), ('77'), (), ('laxman'),
        ('krish'), ('45')]
print(Remove(tuples))
print("**************************************")
print("Answer 18")
test_list = [(1, 4, 5), (7, 8), (2, 4, 10)]
print("The original list is : " + str(test_list))
sum = 0
for sub in test_list:
    for i in sub:
        sum = sum + i
res = sum / len(test_list)
print("The mean of tuple list is : " + str(res))
print("**************************************")
print("Answer 19")
s=input("Enter Your Password:")
l, u, p, d = 0, 0, 0, 0
if (len(s) >= 6 and len(s) <=16):
    for i in s:
        if (i.islower()):
            l+=1           
        if (i.isupper()):
            u+=1           
        if (i.isdigit()):
            d+=1           
        if(i=='@'or i=='$' or i=='#' or i=='_'):
            p+=1          
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
    print("Valid Password")
else:
    print("Invalid Password")
