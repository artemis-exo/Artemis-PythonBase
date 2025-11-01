#Booelans  --> True /False
a=True
a=False
print(type( a))

age =16
is_adult=age>=18
print(is_adult)

#Boolean is a Subclass of Integer
print(True==1)
print(False==0)

print(True+True)
print(True + True + False +8)

print(int(True))
print(int(False))

#Truthy or Falsy
print(bool(1))
print(bool(0))
print(bool("hffhu"))  # if anything is written with boolean it will give either true or false
print(bool(0))

#Falsy values in Python
print(bool(0))
print(bool(0.0))
print(bool(''))    # Empty String
print(bool([]))    #Empty List
print(bool({}))    # Empty dictionary
print(bool(None))

#All other values are Truthy
print(bool(42))
print(bool(-1))
print(bool("Hello"))
print(bool([1,2]))

# Every Boolean is an Integer
print(isinstance(True,int))   # It is a built-in function used to check if an object is an instance of specified class or type

# Every Integer is a Boolean --> False
print(isinstance(1,bool))

a,b=102,10
print(a.bit_length()) # method to determine the number of bits required to represent an Integer
print(b.bit_length())
print(True.bit_length())  # Bits require to show --> 1
print(False.bit_length()) # Bits required to show --> 1

# LOGICAL OPERATORS
# 1. Logical AND
has_addhar=True
age=17
print(has_addhar and age>=18 )

# 2. Logical OR
has_addhar=True
has_dl=False
print(has_addhar or has_dl)

# 3. Logical NOT
has_injury=True
print(not has_injury)

age=24
income=32000
print(age<18 or not(income>50000))

# Boolean operator Precedence
# not > and > or
result = True or False and not True
print(result)

result1=(True or False) and (not True)
print(result1)

age=24
income =36000
credit_score=900
is_eligible=(age>=18 and age<=66) and (income>24000 or credit_score>650)
print(is_eligible)

working_age=18<=age<=65  # this is cleaner than above
print(working_age)