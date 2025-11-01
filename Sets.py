# What is set
# Unordered, Unindexed, Mutable, Unique
# Union, intersection, difference
# fast membership testing
# Should have immutable items
# Can store Heterogeneous values
# Curly braces are used to denote a set
# Python sets are directly inspired by Mathematical concept

# Creating a Set
# A. Set Literals {}
# B. set() Constructor

numbers={1,2,3,4,5}
names={"Alice","Bob","Charlie"}
mixed={1,"Alice","Bob","Charlie",3,5,6,7}
print(numbers)
print(names)
print(mixed)

# Empty set- IMPORTANT: you cannot use {} for empty set
# e={} - This creates an empty dictionary, not a set
e=set()
s={1,1,2,3,4,4,6,6,7,8}
print(s)

t={1,"Hello",True,(1,2,3,4)} # On adding a list it is displaying an error
print(t)

# The set() function creates a set from an iterable (Like a list, tuple, or string)
list_data=[1,2,3,2,1,4]
set_from_list=set(list_data)
print(set_from_list)
print("size of set",len(set_from_list))

text="Hello"
set_from_string=set(text)
print(set_from_string)

tuple_data=(1,2,3,2,1,4)
set_from_tuple=set(tuple_data)
print(set_from_tuple)

empty_set=set()
print(type(empty_set))
print(len(empty_set))

s=set(range(1,7))
print(s)

# Set Operations
#add - method can add only one
# update -for iterable
my_set={1,2,3}
print("Original:",my_set)
my_set.add(4)
print("After adding:",my_set)
my_set.add((0,9,8))
print("After adding again:",my_set)
# Using update() to add multiple elements
my_set.update([5,6,7])
print("After updating with list:",my_set)
my_set.update("abc")
print("After updating with string:",my_set)

my_set.update([12,13],{14,15},"abc")
print("After multiple updates:",my_set)

'''
remove(element): Removes element, raises KeyError if not found
discard(element): discards element, does nothing  if not found
pop(): Removes and return an arbitrary element
clear(): Removes all-elements

'''
my_new={1,2,3,4,5,"a","b","c"}
print("Original:",my_new)
my_new.remove(1)
print(my_new)
# my_new.remove(23) - in this it will display an error

my_new.discard(33)  # No error in this discard method
print(my_new)

print(my_new.pop())
print(my_new)

fruits={"apple","banana","orange","strawberry"}
print("apple"in fruits)

# Fast membership Testing
import time
large_list=list(range(10000000))
large_set=set(range(10000000))
search_value=99999

start_time = time.time()
result_list=search_value in large_list
list_time=time.time()-start_time

start_time = time.time()
result_set=search_value in large_set
set_time=time.time()-start_time

print(f"List search time: {list_time} seconds")
print(f"Set search time: {set_time} seconds")  # it takes lesser time than list

# Mathematical Set Operations
# 1. Union
set_a={1,2,3,4}
set_b={3,4,5,6,7}
# Pipe Operator is used for Union and can only used with sets
union_res1=set_a | set_b
print("Union using |:",union_res1)
union_res2=set_a.union(set_b)
print("Union using union():",union_res2)

set_c={5,6,7,8,9}
union_res3=set_c | set_b | set_a
print("Multiple Union using |:",union_res3)

# Union with other iterables (only union() method)
union_with_list=set_a.union([10,11,12])
print("Union using union():",union_with_list)

user1_interest={"movies","books","music"}
user2_interest={"music","sports","travelling"}
user3_interest={"mma","cooking","travelling"}

all_interest=user1_interest|user2_interest|user3_interest
print("All interest:",all_interest)

# 2. Intersection
set1={1,2,3,4,5}
set2={4,5,6,7,8,1}
# And Operator is used for intersection and can used with sets
intersection=set1&set2
print("Intersection:",intersection)
intersection1=set1.intersection(set2)
print("Intersection:",intersection1)

set3={3,4,5,9,10}
intersection_multiple=set1 & set2 & set3
print("Intersection_multiple:",intersection_multiple)

set4={10,11,12}
intersections=set1 & set4
print("Intersections:",intersections)  # display empty set

dev1_skills={"python","java","sql","git"}
dev2_skills={"python","javaScript","sql","docker"}
dev3_skills={"python","mongoDB","sql","react"}

print(dev1_skills & dev2_skills & dev3_skills)

# Difference
setA={1,2,3,4,5}
setB={3,4,5,6,7}
difference1=setA.difference(setB)
print("Difference:",difference1)

differnce2=setA-setB
print("Difference2 using A-B:",differnce2)

differnce3=setB-setA
print("Difference3 using B-A:",differnce3)

setC={2,3,9,10}
difference_multiple=setA-setB-setC
print("Difference_multiple:",difference_multiple)

# Symmetric Difference -  Common will be removed
set_a={1,2,3,4,5}
set_b={3,4,5,6,7}
sym_difference=set_a^set_b
print("Sym difference using a^b:",sym_difference)

sym_difference2=set_a.symmetric_difference(set_b)
print("Sym difference2:",sym_difference2)

# Subset And Superset
set_a={1,2,3}
set_b={1,2,3,4,5}
set_c={1,2}

print("A is subset of B:",set_a.issubset(set_b))
print("B is subset of A:",set_b.issubset(set_a))
print("C is subset of A:",set_c.issubset(set_a))

print("B is superset of A:",set_b.issuperset(set_a))
print("A is superset of B:",set_a.issuperset(set_b))
print("A is superset of C:",set_a.issuperset(set_c))

# <= operator
# This operator checks if the left set is a subset of (or equal to) the right set.

print("A <=B:", set_a <= set_b)
print("A <= A:", set_a <= set_a)
print("C <= A:", set_c <= set_a)
print("C < A:", set_c < set_a)
print("A < A:", set_a < set_a)

# Disjoint set
set_a={1,2,3}
set_b={4,5,6}
set_c={3,4,5}
print("A and B are disjoint",set_a.isdisjoint(set_b))
print("B and C are disjoint",set_b.isdisjoint(set_c))
print("A and C are disjoint",set_a.isdisjoint(set_c))
# Same as isdisjoint()
print(len(set_a & set_b)==0)
# Empty set is disjoint with any set

# Copying Sets
original_set={1,2,3}
new_set=original_set # pointing to the same set no copy is created
new_set.add(4)
print(original_set)

new_set=original_set.copy()
new_set.add(5)
print(original_set) # 5 is not added to original set now

# Iteration over sets with loops

set_a={1,2,3}
for i in set_a:
    print(i)

num={1,2,3,4,5}
for i in num:
    if i % 2 == 0:
        print(i)

# Frozen Sets - Frozensets are immutable versions of sets
# Supports only read-only operations
# Frozen set are Hashable
# Can be dict/ set key - yes can be used as dictionary keys
# Only read only methods can be used

regular_set={1,2,3,4,5}
frozen_set=frozenset(regular_set)

print("Regular set:",regular_set)
print("Frozen set:",frozen_set)
print("Type:",type(frozen_set))

print("Length:",len(frozen_set))
print("Membership:", 3 in frozen_set)
print("Union:",frozen_set |{5,6})
print("Intersection:",frozen_set & {2,3,4,5})

# frozen_set.add(5)
# frozen_set.remove(1)

mutable_set={1,2,3}
immutable_set=frozenset([1,2,3])

print("Sets are equal:", mutable_set == immutable_set)
#print(hash(mutable_set))
print(hash(immutable_set))



