print("Assignment 1 !")
print("Answer 1")
string=input("Enter a string: ")
print("Length of string =",len(string))
print("*****************************************")
print("Answer 2")
string="python hypo"
countp=string.count('p')
county=string.count('y')
countt=string.count('t')
counth=string.count('h')
counto=string.count('o')
countn=string.count('n')
print('p:',countp,' y:',county,'t:',countt,' h:',counth,'o:',counto,' n:',countn)
print("*****************************************")
print("Answer 3")
string=input("Enter the string:")
l=len(string)
if(l>=2):
 p=string[:2]
 q=string[-2:]
 print(p+q)
else:
 print("Empty string")
print("*****************************************")
print("Answer 4")
string=input("Enter the string:")
first=string[0]
for x in range (1,len(string)):
    if (first==string[x]):
        item=string[x]
        string=string.replace(item,'$')
print(first+string[1:])
print("*****************************************")
print("Answer 5")
string1=input("Enter 1st string:")
string2=input("Enter 2nd string:")
item1=string1[0]
item2=string2[0]
string1=string1.replace(item1,item2)
string2=string2.replace(item2,item1)
print(string1, string2)
print("*****************************************")
print("Answer 6")
string=input("Enter the string:")
l=len(string)
if(l>=3):
    if(string[-3:]=='ing'):
     print(string+'ly')
    else:
     print(string+'ing')
else:
 print(string)
print("*****************************************")
print("Answer 7")
string=input("Enter the string:")
snot=string.find('not')
spoor=string.find('poor')
if spoor>snot and snot>0 and spoor>0:
 string=string.replace(string[snot:(spoor+4)],'good')
 print(string)
else:
 print(string)
print("*****************************************")
print("Answer 8")
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["pumori","ritu","prachi","shubham"])
print("Longest word: ",result[1])
print("Length of the longest word: ",result[0])
print("*****************************************")
print("Answer 9")
str="online tutorial is best"
n=input("Enter the index)
first_part= str[0:n]
second_part= str[n+1:]
print(first_part + " " + second_part)
print("*****************************************")
print("Answer 10")
def word(str):
  str=str[-1:] + str[1:-1] + str[:1]
  print(str)
item=input("Enter the string")
print(word(item))
print("*****************************************")
print("Answer 11")
def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
item=input("Enter the string")
print(odd_values_string(item))
print("*****************************************")
print("Answer 12")
def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print( word_count('the Golden Temple is the holy place for sikh'))
print("*****************************************")
print("Answer 13")
user_input=input("what is ur name?")
print("what is ur name?",user_input.lower())
print("what is ur name?",user_input.upper())
print("*****************************************")
print("Answer 14")
items = input("Input comma separated sequence of words ")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))
print("*****************************************")
print("Answer 15")
def add_tags(tag,word):
    print("<",tag,">",word,"</",tag,">")
intag=input("Enter Tag:")
inword=input("Enter word:")
add_tags(intag,inword)
print("*****************************************")
print("Answer 16")
def stringmiddle(string,word):
   return string[:2]+ word + string[2:]
print(stringmiddle('I fine','am '))
print("*****************************************")
print("Answer 17")
string=input("Enter the word:")
if(len(string)>2):
   print(string[-2:]+string[-2:]+string[-2:]+string[-2:])
else:
    print("Word contains only 2 characters")
print("*****************************************")
print("Answer 18")
string=input("Enter the word:")
if(len(string)>3):
   print(string[:3])
else:
    print(string)
print("*****************************************")
print("Answer 19")
string=input("Enter the word:")
pos=input("Enter Position:")
pos=int(pos)
if(len(string)>pos):
   print(string[pos:])
else:
   print("Invalid entry")
print("*****************************************")
print("Answer 20")
string=input("Enter the string:")
if(len(string)%4==0):
   print(string[::-1])
else:
   print("not a multiple of 4")
print("*****************************************")
print("Answer 21")
def to_upper(string):
  upp=0
  for letter in string[:4]:
    if letter.upper()==letter:
     upp+=1
  if upp>=2:
      return string.upper()
  return string
string0=input("Enter the string:")
print(to_upper(string0))
print("*****************************************")
print("Answer 23")
string="India is my country"
first=string[0]
fin=input("Enter first character:")
if fin==first:
    print("First Character matched")
else:
    print("First character didn't matched")
print("String is ",string)









    
 
 
           


