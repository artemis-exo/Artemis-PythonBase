# A Tuple is an ordered, immutable collection of items
# We can also form tuple by using comma separated vales not always by ()
# Tuples are created are using comas, not parentheses
# Trailing commas in multi-element tuples are optional
my_tuple=(1,2,3,4,5)
my_tuple_1=1,2,3,4,5
print(type(my_tuple_1))
a=(1,) # tuple
print(type(a))
b=(1)
print(type(b)) # not tuple

tuple_from_string=tuple("HELLO")
print(tuple_from_string)   #('H', 'E', 'L', 'L', 'O')

tuple_from_list=tuple([1,2,3,4,5])
print(tuple_from_list)  #(1, 2, 3, 4, 5)

# t= tuple(5)  type_error : 'int' object is not iterable
t=tuple([5])
print(t)

# Empty Tuple
empty=()
print(type(empty))

# Key Difference from Lists
# 1 Tuples are immutable
# 2 Tuples use parentheses and List use square brackets
# 3 Tuples are generally smaller and faster than lists
t=(1,2,3)
 # t[0]=11 these are immutable

import sys
print(sys.getsizeof((1,2,3))) # Less bytes
print(sys.getsizeof([1,2,3])) # More bytes

# Immutability applies to the tuple container, not to the objects inside it
# Immutable tuples can be used as keys in dictionaries or stored in sets
t=(1,[2,3])
t[1].append(4)
print(t)

orig_tupel=(1,2,3)
new_tuple=orig_tupel+(4,5)
print(new_tuple)  #(1, 2, 3, 4, 5)

orignal_tupel=(1,2,3)
print(orignal_tupel+(6,7))
print(orignal_tupel)  # Remains immutable

orignal_tupel=(1,2,3)
original_tupel=orignal_tupel+(4,5)
print(original_tupel)   # (1, 2, 3, 4, 5)

# Accessing Tuple Elements
fruits=("apple","banana","orange","strawberry")
print(fruits[0])
print(fruits[-2])

# Slicing
print(fruits[1:3])
print(fruits[::-1])  # Reverse Tuple

nested_tuple=((1,2),(3,4),(5,6))
print(nested_tuple[0][1])

t=(44,"hello",[1,2,3],{'key':"value"})
print(t[3])
print(t[3]['key'])   #value

# Unpacking Tuple
# Tuple unpacking allows you to assign tuple elements to individual variables in a single operations
p= 1,2,3
print(type(p))
a,b,c=p
print(a,b,c)
# Python does this by matching the structure (number of items ) on both sides of the assignment

a,*b,c=1,2,3,4,5,6
print(a,b,c)

a,*b,c,d="hello"
print(a,b,c,d)

nested_tuple=((1,2),(3,4),(5,6))
a,b,c=nested_tuple
print(a,b,c)

# Iterating Tuples
fruits=("apple","banana","orange","strawberry")
for fruit in fruits:
    print(fruit)

colors=("red","green","blue","yellow")
for color in enumerate(colors):
    print(color)

for index, color in enumerate(colors):
    print(index,color)
print()

for index, color in enumerate(colors, start=14):
    print(index,color)

pairs=[(1,'a'),(2,'b'),(3,'c')]
for num,let in pairs:
    print(num,let)

# Concatenation and repeatation
tuple1=('a',)
result=tuple1*3
print(result)

# Tuple Methods - Count and Index








