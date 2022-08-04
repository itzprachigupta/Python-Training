f=open('file_handling.txt','w')
str='This is a demo file to perform different file handling operations.'
f.write(str)
f.close()

g=open('file_handling.txt','r')
r=g.read()
print(f"Reading from file in r mode:\n{r}")
g.close()

h=open('file_handling.txt','a')
str1='\nThis is append function'
h.write(str1)
h.close()

i=open('file_handling.txt','r+')
i.seek(91)
i.write("\nwriting in r+ mode")
i.writelines("\nwriting\nusing\nwritelines\n")
i.seek(0)
z=i.read()
print(f"\nReading from file in r+ mode:\n{z}")
i.close()

i=open('file_handling.txt','a+')
i.write("\nwriting in a+ mode")
i.writelines("\nwriting\nusing\nwritelines\n")
i.seek(0)
z=i.read()
print(f"Reading from file in a+ mode:\n{z}")
i.close()







