print("Hello World")
'''
RAM is a Volatile, and all its content are lost once a Program terminates in order to Persist the data forever, we use files

A file is a data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it.

HDD= Non Volatile

Type of Files
1. Text files
2. Binary files

Modes of openning files
r - Read a file
w - Write a file
a - Append a file
+ - open for updating
rb - Read a binary file
rt - will open for read in text mode
'''
# It is by default r means read only and w means Write
f=open("myfile.txt")

# lines=f.readlines()
# print(lines,type(lines))  # it is a List

# line1=f.readline()
# print(line1,type(line1))
#
# line2=f.readline()
# print(line2,type(line2))
#
# line3=f.readline()
# print(line3,type(line3))
#
# line4=f.readline()
# print(line4,type(line4))
# print(line4=="")
# f.close()

# Same using while Loop
line5=f.readline()
while line5!="":
    print(line5)
    line5=f.readline()

f.close()

# f=open("texto.txt","w")
# f.write("Hello World Hoomans")
# f.close()

f=open("texto.txt","r")
print(f.read())
f.close()

# Same can be written using with statement like this automatically closes the file
# And we don't have to explicitly close the file in this
with open("texto.txt") as f:
    print(f.read())
