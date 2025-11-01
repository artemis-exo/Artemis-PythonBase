def intro(firstName,lastName,country):
    print("Hello")
    print(f"My name is {firstName} {lastName}")
    print(f"I live in {country}")
    print("Bye !")

intro("Vedaant","Bisht","India")
res= intro("Vedaant","Bisht","India")
print(res)  # none because we return nothing

def sumSqaure(a,b):
    return((a+b)**2)

res=sumSqaure(10,20)
print(res)

def divide(a,b):
    if(b==0):
        return None
    else:
        return a/b

print(divide(10,20))

def SumEven(li):
    '''
    It will return sum of Even Numbers'''
    sum=0
    for x in li:
        if x % 2 == 0:
            sum=sum+x
    return sum

print(SumEven([1,2,3,4,5,6,7,8]))

def akno(firstName,lastName="Bisht",country="Space"):
    print("Hello")
    print(f"My name is {firstName} {lastName}")
    print(f"I live in {country}")
    print("Bye !")
akno("Human")

# KEYWORD ARGUMENTS
def divide(a,b):
    if(b==0):
        return None
    else:
        return a/b

print(divide(b=10,a=50))  # Keyword arguments
print(divide(10,b=5)) # must pass positional arguments before keyword arguments

def akno(firstName="Homo",lastName="Sapien",country="Space"):
    print("Hello")
    print(f"My name is {firstName} {lastName}")
    print(f"I live in {country}")
    print("Bye !")
akno(country="India")

def fun():
    return 1,2,3,4,5,6  # Comma separated values formed Tuple

def func2():
    return "Hello",12, True

x=fun()
print(x)
print(type(x))
print(func2())

print(SumEven.__doc__) # Returns the documentation of the function

# ARGS
# Single * means accumulate items
# Args grabs Positional Arguments
def sums(msg,*nums):
    print(type(nums))
    print(msg)
    sum=0
    for i in nums:
        sum=sum+i
    return sum

print(sums("I am calculating sum",1,2,3,5,7,89))

#KWARGS
# Kwargs grabs Keyword Arguments
# Double ** means accumulate Key value pairs
def build_profile(**things):
    print("Building profile...")
    print(things)
    print(type(things)) # It is a collection of pairs
    for i, j in things.items():
        print(f"{i}:{j}")

build_profile(name="Vedaant",age=21,designation="student",hobbies=["Badminton"])

# All together
def mixed(msg1,msg2,*things,**kwargs):
    print(msg1)
    print(msg2)
    print(things)
    print(kwargs)

mixed("Example1", "Example2",1,2,3,4, name="Vedaant",role="Student")

# Can also be used While calling
def add(x,y,z):
    return x + y + z

vals=[1,2,3]
print(add(*vals))

params={'x':10,'y':20,'z':30} # Function should have the same args as of keys in dictionary
print(add(**params))

# FUNCTION SCOPE
a=1  # Global Variable
# Variables created outside all the functions exist throughout the entire program.
def funct():
    a=14  # Local Variable
    # Variables created inside a function exists only within the function
    print(f"value of a is {a}")
funct()
print(f"value of a is {a}")

name="Vedaant"
def outer_func():
    name="Alice"
    def inner_func():
        name="Bob"
        print(f"Inner function: {name}")
    inner_func()
    print(f"Outer function: {name}")
outer_func()
print(f"Global scope: {name}")

counter =0
def increament():
    global counter  # Will display error if not write global counter
    counter=counter+1
    print(f"Counter: {counter}")
def reset():
    global counter # if iam adding Global it will reseting it as 0
    counter=0
increament()
increament()
reset()
increament()
print(f"Counter_out: {counter}")

x=10
y=20
z=30
def modify_globals():
    global x,y    # Create a new global variable
    x=100
    y=200
    z=300
modify_globals()
print(f"x={x}, y={y}, z={z}")

def outer_function():
    x=10
    def inner_function():
        nonlocal x
        x=20
        print(f"Inner function: {x}")
    print(f"Before inner function: {x}")
    inner_function()
    print(f"After inner function: {x}")
outer_function()

def create():
    functions=[]
    for i in range(3):
        def func():
            return i
        functions.append(func)
    return functions
funcs=create()
for func in funcs:
    print(func())

def demonstrate_lifetime():
    print("Function called - local variables created")
    local_var="I exists only during function execution"
    print(f"Local variable: {local_var}")
    print("Function ending - local variables destroyed")

print("Before function call")
demonstrate_lifetime()
print("After function call")
#print(local_var)

# Global variables: Exists for the entire program execution
# Local variables: are created when function is called, destroyed when function ends
# Enclosing variables : Exists as long as there are references to them

# Enclosing Example
def outer():
    message="hello"
    def inner():
        return message  # uses a variable from outer
    return inner
f=outer()    # outer() is done now
print(f())     # prints "hello"

# BUILT - IN FUNCTIONS

# Type Conversion functions
number_str="44"
number_int=int(number_str)
print(type(number_int))

price=(float)("19.99")
print(type(price))
age=24
age_str=str(age)
print(type(age_str))

print(bool(1))  #True
print(bool(0))  #False
print(bool("")) #False
print(bool("hi"))# True

numbers=(1,2,3,4,5)
numbers_list=list(numbers)
print(numbers_list)
numbers_set=set(numbers)
print(numbers_set)

# round()- round to nearest integer or specified decimal value
print(round(3.7))  # Output: 4
print(round(3.14159,2))  # Output: 3.14

# min() and max()- find minimum and maximum
numbers=[10,5,8,20,3]
print(min(numbers))
print(max(numbers))
print(min(10,5,8))

# sum()- sum of all elements
print(sum(numbers))
print(sum([1,2,3],10))

# pow() - power function
print(pow(2,3))
print(pow(2,3,5)) # Output: 3(2^3 % 5)

# Sequence Function
# len() - length of sequence
text="Hello World"
numbers=[1,2,3,4,5]
print(len(numbers))
print(len(text))

# zip() - combines multiple iterables
names=["Alice","Bob","Charlie"]
age=[25,30,36]
for name, age in zip(names, age):
    print(f"{name} is {age} years old")

'''Output
Alice is 25 years old
Bob is 30 years old
Charlie is 36 years old
'''

# Working with map(), filter(), and reduce()

# map(function, iterable)

def square(x):
    return x**2

numbers=[1,2,3,4,5]
squared_numbers=map(square,numbers)
print(set(squared_numbers)) # We have to convert it into list

def add_nums(x,y):
    return x+y
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
result=map(add_nums,list1,list2)
print(list(result))

#Converting String List in Int
string_nums=["1","2","3","4","5"]
li=[int(i) for i in string_nums]  # Using list Comprehension
print(li)

# Or can be done by Map
pi=map(int,string_nums)
print(list(pi))

# Filter Use - It checks the condition and collects the values are satisfying or True to the condition
def is_even(x):
    return x % 2 == 0
numie=[1,2,3,4,5,6,7,8]
even_numbers=filter(is_even,numie)
print(list(even_numbers))

# reduce use- its is a function which repeatedly applies function to the items of iterable so that one single value is outputed
# it is in functools module
# 0 is hidden in this
# it accumulates the values

from functools import reduce
def addie(x,y):
    return x+y
number=[1,2,3,4,5]
total=reduce(addie,number,100)
print(total)

# LAMBDA FUNCTIONS - Anonymous function without name and def keyword
'''
Single expression only (no statements)
No name (anonymous)
Can be assigned to variables
Often used for short, simple operations
Return the result of thier expression automatically
'''
add_lambda=lambda x,y: x+y
print(add_lambda(1,2))

sq_lambda=lambda x: x**2
print(sq_lambda(3))

# Without parameter
greet_lambda=lambda:"Alice"
print(greet_lambda())

power_lambda= lambda x,y=2: x**y
print(power_lambda(2))

celsius_temp=[0,20,30,40]
f_temps=set(map(lambda x: (x*9/5)+32,celsius_temp))
print(f_temps)

numbs=[1,2,3,4,5,6,7,8,9,10]
res=list(filter(lambda x: x%2==0,numbs))
print(res)

# Filter strings longer than 5 characters
words=["apples","oranges","pears","cat","elephant","dog"]
print(list(filter(lambda s: len(s)>5, words)))

# Sort on basis of their marks
student=[('Alice',98), ('Lob',67),('Varlie',93), ('David',80)]
print(sorted(student))  # Sorted on basis of alphabetical order
print(sorted(student,key=lambda x:x[1]))  # On basis of marks
print(sorted(student, reverse=True,key=lambda x:x[1])) # in reverse order

employees=[
    {'name':'John', 'salary': 50000, 'bonus': 5000},
    {'name':'Jane', 'salary': 60000, 'bonus': 7000},
    {'name':'Bob', 'salary': 80000, 'bonus': 6000},
]
print(type(employees))
print(list(map(lambda x: x['salary'] +x['bonus'], employees)))

'''
This won't work - multiple statements
bad_lambda = lambda x: print(x); return x*2

Correct - single expression

Can't have docstrings
Can't use if - elif- else statements
Avoid when there is more complexity
Can use ternary operator
'''
sign_lambda= lambda x: "positive" if x>0 else("negative" if x<0 else "zero")
print(sign_lambda(3))
'''
Output: positive
Output: negative
Output: zero
'''


# FUNCTIONS AS FIRST-CLASS OBJECTS
'''
Being passed as arguments to other functions
Being returned as values from other functions
Being assigned to variables
Being stored in data structures (lists, dictionaries, etc.)
Being created at runtime
'''

def make_multiplier(n):
    def multiplier(x):
        return x*n
    return multiplier

time3=make_multiplier(3)
print(time3(5))  # 15
# times3 contains multiplier function

def greeto(name):
    return f"Hello, {name}!"

say_hello=greeto
print(say_hello("Alice"))
print(greeto("Bob"))
print(say_hello is greeto)

def add(x,y):
    return x+y
def multiply(x,y):
    return x*y
def subtract(x,y):
    return x-y
def divide(x,y):
    return x/y if y!=0 else "Cannot divide by zero"

operations= {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}
print(operations['+'](4,5))
print(operations['*'](4,5))
print(operations['/'](4,5))

def apply_operation(func,x,y):
    return func(x,y)

def addie(a,b):
    return a+b
def multiplyie(a,b):
    return a*b

print(apply_operation(addie,2,3))
print(apply_operation(multiplyie,2,3))











