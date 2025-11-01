# Creating variables in Python
# name, value, memory location ,data type
x=1;
y=type(x)
print(y)
name="Vedaant"
print(type(name))
price=999.99
print(type(price))
is_adult= True
print(type(is_adult))

a=1
b=2
c=3

print(a,b,c,sep=",")  # Adds comma

#Inline declaration
d,e,f,g=3,4,9.9,"Hello"
print(d,   e,f,g,sep=",") #space doesn't matter in variable , it matters in String
print(d+e)

#Variable naming rules
#Letters, digits and underscores
#Must start with _ or letter
#Can't start with number
#Case Sensitive
#Can't use Python Keywords - if,else,while,for,def,class,etc.

name="Akshat"
Name="Ramit"
print(name)
print(Name)

#Python naming conventions

#Snake case

user_name_of_Instagram="The Artemis Aurum"
print(user_name_of_Instagram)

my_string=("Keys of car")
