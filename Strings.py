# String is a sequence of characters enclosed within quotes
from pyexpat.errors import messages

name='Ramesh @#$ 743gcr37r7433848'
print(name)

#Letters, Numbers, Special symbols,Whitespace characters
#Unicode characters
print("\u0061")# small u is followed by 4 digit Unicode
print("\U0001F600")# capital u is followed by 8 digit Unicode

language ="Python"

#  p   y    t    h    o   n
# [0] [1]  [2]  [3]  [4] [5]

print(language)
print(language[4])

print(1+2*3)
print("1+2*3")
print('1+2*3')

name1="Python"
name2='Python'

print(name1==name2)

message="Don't worry about error_s."
print(message)
message='Don\'t worry about errors.' # \ is used to escape this single quote
print(message)

dialogue='She said , "Python is amazing!"'
dialogue="She said, \"Python is amazing!\""
print(dialogue)

poem="The moon climbs high in velvet skies,\n A silver hush where silence lies,\nThe stars lean close with tales to tell,\nOf dreams once cast in wishing wells."
print(poem)

# For multiLine String we need Triple quotes
poem1='''This morning my socks ran away,
Tired of toes and laundry gray.
They leapt from the drawer with flair and might,
  Declared, “We’re off to see the light!'''

print(poem1)

print("HEL\"P")
print("HEL\nP")
print("HEL\tP")
print("He\\lo")

# Printing Directory
# C:\Users\Vedaant\Documents
directory="C:\\Users\\Vedaant\\Documents" #Escape \
print(directory)

#String Concatenation

a="1"
b="1"

print(a+b)

firstName="Vedaant"
lastName="Bisht"
print(firstName+" "+ lastName)

age=21
messagei="My age is" +" "+str(age)
print(messagei)

city="ANKARA"
temp=91
weather="The weather in "+ city +" "+"is"+" "+ str(temp) +"degrees"
print(weather)

#Using f String  this is simple and reliable
weather_rep=f"The tempearture in {city} is {temp*2} degrees"
print(weather_rep)

a=5
b=7
print(f"The sum of {a} and {b} is {a+b}")

name="Vedaant"
print(f"First character of {name} is {name[0]} ")

#This a curly brace: {  print this
print(f"This is a curly brace: }}") #We have to text 2 curly braces to print one

a="PYTHON"
res=a*3
print(f"{res }")

star="*"
print((star*5+ "\n")*5)

a="PYTHON"
print(a*0) #Empty string
print(a)
print(a*-1) #Empty string

#PyPythonthon  -to Print
n="Py"
g="thon"
print(n*2+g*2)
#OR
print("Py"*2+ "thon"*2)

#To find Length
i="Python"
print(len(i))

print(len(""))

print(len("HELLO\nWORLD"))

print(len("❤️")) # Because of two Unicode
print("\u2764")  #White heart
print("\uFE0F")  #Blank
print("\u2764\uFE0F")

msg="Help!"
print(len(msg)==5)
res=len(msg)>=5
print(res)

print("apple"=="apple")
print("apple"=="Apple")
print("apple"=="orange")
print('apple'!="orange")

#Lexicography Check
print("a"<"b")
print("apple"<"banana")
print("apple">"Apple")  #Uppercase letters are smaller than Lowercase
print("apple"<"ape")

#Unicode / ASCII value
print(ord("a"))
print(ord("A"))
print("\u0061") #Hexadecimal value of 97
print(chr(97))

# 143,000 --> Total characters
# 128 character --> ASCII a-z,A-Z, 0-9, Punctuation, control

#String Indexing and Slicing

#INDEXING
txt="Python"
# print(txt[len(txt)]) --> will give error index out of bound

print(txt[len(txt)-1])  # ---> Subtract 1 from the Index of String Array

'''
String:   P   Y   T   H    O    N
Index:    0   1   2   3    4    5
Neg Idx: -6  -5  -4  -3   -2   -1  
'''
print(txt[-1])

#SLICING

#string[start:end]
#start - inclusive
#end - exclusive

txt="Python Programming"
slice = txt[0:6] # It neglects the last character so we take 1 extra (6) like here
print(slice)

#For printing only programming
print(txt[7:18])
print(txt[7:])  # Also the same output
print(txt[:]) # Full string

#Using Negative Index
print(txt[-11:-1])

# We need PTO in Python Programming
print(txt[:6:2]) # Last 2 determines that we are taking index of sliced index after every 2

# A Negative step traverses the string in reverse direction
print(txt[::-2]) # From Negative taking from End, and also Skiping every 2 letter

#Reverse String
#gnimmargorP nohtyP
print(txt[::-1])

#String Methods
print(txt.upper())  # Prints all in upperCase
print(txt.lower())

txt="hello python programming"
print(txt.title()) #Prints the first letter after Space in Uppercase
print(txt.capitalize())  # only First character Capital

#For removing Spaces
txt="     hello python programming      "
print(txt.strip()) # Removes all the spaces form back and front
print(txt.lstrip()) # Removes spaces only from left i.e. hello side
print(txt.rstrip()) # Removes spaces only from right i.e. programming side

#For Finding
txt="Python is amazing, Python is fun"
idx=txt.find("Python")
idn=txt.find("python")

print(idx)
print(idn)  # Will return -1 because python is not found--> (p)
print(txt.find("fun"))
print(txt.find("is",19))

#FOR COUNTING
#string.count(substring,start,end)
print(txt.count("python"))
print(txt.count("Python"))

email="vedaantbisht.gmail.com"
print(email.find("@")==-1)

#REPLACEMENT
#string.replace(old,new,count)
txt ="Hello World"
print(txt.replace("World","Python"))
text="banana banana banana"
print(text.replace("banana","apple")) # All get replaced
print(text.replace("banana","apple",2)) #Only 2 apple gets replaced

#Checking Alphabets
# string.isalpha
text1="Python"
text2="Python 3"
print(text1.isalpha())
print(text2.isalpha())

#Checking Digits
# string.isdigit
text1="23243"
text2="2python"
print(text1.isdigit())
print(text2.isdigit())

#Checking AlphaNumeric
#String.isalnum
text1="Python347"
text2="python"
text3="python 327"
print(text1.isalnum())
print(text2.isalnum())
print(text3.isalnum()) #    because of adding spaces alnum gives a false value

#Checking UpperCase and LowerCase
#string.islower()
tot="goal"
print(tot.islower())
print(tot.isupper())

#string.isupper()
tot="Python"
tool="COOL"
print(tot.isupper())  #False
print(tool.isupper())  #True

# Checking Spaces
tot= "    "
tot1="    ,"
print(tot.isspace())
print(tot1.isspace())
# Starts WIth ends with
go="Python is amazing"
print(go.startswith("Python"))  #True
print(go.endswith("Amazing"))  # False because of A is in upperCase

#Split
text="apple,banana,orange,grape"
print(text.split(","))
sen="Python is fun to learn"
print(sen.split(","))

li=['apple', 'banana', 'orange', 'grape']
print(",".join(li))

# .format() Method
name="Vedaant"
message= "Hello, My name is {} and my age is -{}".format(name,78)
message1= "Hello, My name is {1} and my age is {0}".format(name,78) # 1 and 0 and swap the parameters position
message2= "Hello, My name is {p1} and my age is {p2}".format(p1=name,p2=64)  #Place holder
print(message)
print(message1)
print(message2)
print("Hello Venella Iam from {} time and my name is {}".format(1200,"casper"))


#String Immutability

s="HELLO"
print(id(s))   # Prints the address of string
#s[0]="M"  THis won't work
print("M"+ s[1:])  # String is immutable so we have to use Slicing
s="M"+ s[1:]
print(id(s))  # This address is MELLO address

#RAW STRINGS
rs= r"He\nllo"  #It doesn't expect after backlash
print(rs)
print(r"C:\Users\Name\Documents")

r"She said, \"Hello\"" # Works: backslash escapes the quote
print(r"She said, \"Hello\"")
#r"She said, "Hello""    #Syntax Error:qoute ends the string too
r"This ends with a\\"   #Works - treated as closing
#r"This ends with a\\\"  #Syntax error
#r"This ends with a\"  #Syntax error
r"This ends with a \""  # Works

# odd --> escape closing quote
# even --> doesn't escape closing quote

# 1. String Method Changing
# strip, capitalize the first letter of each word, and replace "Skill" with "Expertise"
text="python programming SKILLS"
text=text.strip() # Removes all the space from back and front
print(text)
text= text.title()  # All the elements after the space should be capital
print(text)
text= text.replace("Skills","Expertise")
print(text)

#Or by Method Chaining
print(text.strip().title().replace("Skills","Expertise"))

# 2. Print every second letter using slicing
tam= "Python Programming Language"
print(tam[::2])

# 3.Print the string in reverse order using Slicing
print(tam[::-1])

#4. Extract and print just "Programming in Negative indices"
print(tam[-20:-9])

#String Concatenation and Slicing
#5. Create a new string by extracting the first letter of each word and concatenate them
tol= "Python is easy to learn"
res= tol[0]+tol[7]+tol[10]+tol[15]+tol[18]
print(res)

# 6. String palindrome check
# example - pop , Radar
yolo="radar"
print(yolo==yolo[::-1])

# 7. Find occurrence of 'i','s','p', and 'm'
tex="mississippi"
count_i=tex.count("i")
count_s=tex.count("s")
count_p=tex.count("p")
count_m=tex.count("m")

print(f"i:{count_i}")
print(f"s:{count_s}")
print(f"p:{count_p}")
print(f"m:{count_m}")


