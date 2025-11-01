# A built-in DS that stores an ordered, mutable collection of items
# Lists can hold items of any type, including other lists

# Ordered: Items have a defined order and can accessed by their index
# Mutable: You can change, add or remove items after the list has been created
# Heterogeneous: A single list can contain elements of different data types.
# Iterable: Lists can be looped over using for loops or comprehensions

my_list=[1,2,3,4,5]
mixed_list=[1,"Hello",3.14, True]
nested =[[1,2,3],[4,5,6],[7,8,9]]

# Empty list
empty=[]

# List of strings
colors=["red","green","blue"]

# List of booleans
staf=[True,False,True]

# Mixed LIst
mixed_list=[1,"Hello",3.14, True]

# List inside a list (nested)
nested =[[1,2,3],[4,5,6],[7,8,9]]

li= list()     # List constructor
print(type(staf))
print(type(li))

li=list("HELLO")   # Have give some iterable
print(li)

s={10,20,30}
lst=list(s)
print(lst)

print(list(range(10)))

original_list=[3,4,6,777]
copied_list=original_list
print(copied_list)

# Indexing and Slicing of List
fruits=["apple","banana","orange"]
print(fruits[-2])

num=[10,20,30,40,50]
# List[start:end:step]
print(num[0:3])
print(num[1::2])
print(num[0:22])  # Complete list it doesn't throw error
print(num[len(num)-1]) # if we want fetch an element without slicing so we use length

# ex - reverse a String
print(num[::-1])

print(num[-3:])

# Modifying Lists
fruits=["apple","banana","cherry"]
fruits[1]="blueberry"
print(fruits)

fruits.append("orange")
print(fruits)   # ['apple', 'blueberry', 'cherry', 'orange']

# for inserting
fruits.insert(3,"banana")
print(fruits)    # ['apple', 'blueberry', 'cherry', 'banana', 'orange']

# For adding and extending
fruits_2=["grapes","kiwi"]
fruits.extend(fruits_2) # if we use append , would add the entire list as a element , in this it is added to the existing String
print(fruits)

# For removing
fruits.remove("blueberry")  # it removes by name
print(fruits)  # ['apple', 'cherry', 'banana', 'orange', 'grapes', 'kiwi']

# For removing using Index
fruits.pop(2)  # ['apple', 'cherry', 'orange', 'grapes', 'kiwi']   if no index given then the last one will be removed
print(fruits)

# Delete Keyword
# It allows us to do slicing
del fruits[1:3]
print(fruits)  # ['apple', 'grapes', 'kiwi']

# For clearing
fruits.clear()
print(fruits)

# Shallow vs Deep copy
a=[1,2,3,4]
b=a
b.append(4) # - b is pointing where a is pointing
a.append(5)
print(a)
print(b)# [1, 2, 3, 4] in a

#using slicing
a=[1,2,3]
b=a[:]   # Shallow copy of flat list  slicing creates a new copy
b.append(4)
print(a)    # [1, 2, 3]
print(b)    # [1, 2, 3, 4]

a=[[1,2],[3,4]]
print(a[0][1])   # 2

a=[[1,2],[3,4]]
b=a[:]
b[0][0]=99
print(a)  #   [[99, 2], [3, 4]]
print(b)  #    [[99, 2], [3, 4]]
print(id(a[0]),id(b[0]))  # Pointing same address

# .. List operations
a=[1,2,3]
b=[4,5]
result=a+b
print(result)
result_1=a+b+[6]
print(result_1)

a=[0,1]
print(a*3)

fruits=["apple","banana","orange"]
print("apple" in fruits)
print("kiwi" in fruits)

# list in list
nested=[[0]*3]*3
print(nested)
nested[0][0]=1
print(nested)

# BUILT-IN FUNCTIONS FOR LIST
number=[10,5,8,3]
print(min(number))
print(max(number))
name=["Vedaant","Madhav","Siddharth","Rajat"]
print(max(name))  # Vedaant
print(min(name))  # Madhav

# REVERSING AND SORTING LIST
nums=[1,2,3]
nums.reverse()
print(nums) # it mutates the original List

print(list(reversed(nums))) # it creates a new List

words=["banana","apple","pineapple","watermelon","pomegranate"]
words.sort() # in ascending order
print(words)

words.sort(reverse=True) # in descending order
print(words)

words.sort(key=len,reverse=True)  # On basis of length
print(words)

words=["banana","apple","pineapple","watermelon","pomegranate"]
sorted_words=sorted(words,key=len,reverse=True)
print(sorted_words) # Sorted is used for creating new list and keeping the older one intact

numie=[-10,5,-4,6,-7]
numie.sort(key=abs) # on basis of absolute value
print(numie)

frooty=["apple","banana","orange","apple","guava","banana","apple"]
print(frooty[1:4].count("apple"))
print(frooty.count("kiwi"))
print(frooty.index("banana",2))

# ITERATING THROUGH LISTS
for froo in frooty:
    print(froo)
print()

for i in range(len(frooty)):
    print(frooty[i])

# counting apple in frooty
c=0
for froo in frooty:
    if froo=="apple":
        c+=1
print(c)

# For finding index of orange
f_index=0
for i in range(len(frooty)):
    if frooty[i]=="orange":
        f_index=i
        break
print(f_index)

# For reversing frooty
reversed_list=[]
for rev in frooty[::-1]:
    reversed_list.append(rev)
print(reversed_list)

# same using range
frooty=["apple","banana","orange","apple","guava","banana","apple"]
reverse_list=[]
for i in range (len(frooty)-1,-1,-1):
    reverse_list.append(frooty[i])
print(reverse_list)

# Finding minimum number in list
numb=[45,2,8,1,99,45,3]
min_num=numb[0]
for i in numb:
    if min_num>i:
        min_num=i
print(min_num)

# NESTED LIST
numbers=[1,2,3,4]  # 1D Matrix

matrix=[[1,2,3],  # 2D Matrix
        [4,5,6],
        [7,8,9]]


for row in matrix:
    for x in row:
        print(x,end=" ")
    print()

print()

# Now using Index method
matrix[0][0]=14
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j],end=" ")
    print()

cube=([[1,2],[3,4]],
      [[5,6],[7,8]])
cube[1][1][0]=16
print(cube)

# == VS is Operator
a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is b)  # False in condition of when b=[1,2,3] and True when b=a

a=[1,2,3]
b=a
b.append(4)
print(a)

# List Comprehension
# Squares of list
li=[1,2,3,4,5,6,7]
res=[]

for i in li:
    res.append(i**2)
print(res)

# List comprehension Syntax
# New_list=[expression for item i iterable]
res=[i**2 for i in li]
print(res)

# Even numbers squares from 1-10
rep=[i**2 for i in range(1,11) if i%2==0]
print(rep)

# if else too
rek=[i**2 if i%2==0 else i for i in range(1,11)]
print(rek)

# Each drink with every desert
drinks=['coffee','tea']
deserts=['cake','cookie','ice-cream']
ram=[]
for i in drinks:
    for j in deserts:
        ram.append((i,j))
print(ram)

# OR
ram=[(i,j) for i in drinks for j in deserts]
print(ram)

# Question

matrix=[[1,2,3],  # 2D Matrix
        [4,5,6],
        [7,8,9]]

rse=[j for i in matrix for j in i]
print(rse)

# String in UpperCase
text="Python list comprehension is powerful and concise"
res=[]
for i in text.split():
    if len(i)>5:
      res.append(i.upper())
print(res)

#OR
res=[i.upper() for i in text.split() if len(i)>5]
print(res)








