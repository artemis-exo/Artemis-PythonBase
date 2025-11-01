# keys must be unique - No duplicate keys allowed
# Keys must be immutable - Strings, numbers,tuples can be keys
# Dictionary is based on Hash Table
# Hash Table ---> special type of array it is a data structure where every key has a unique number generate

student={
    "name":"Varshita",
    "age":21,
    "grade":"B",
    "phone_number":"36438231",
    "place_of_birth": "New York"
}
print(student["name"])

fruits= {
    "apple":"red",
    "banana":"yellow",
    "guava":"green"
}
print(fruits["banana"])

dict(apple="red",banana="yellow",kiwi="brown")

d= dict([("apple","red"),("banana","yellow"),("kiwi","brown")])
print(d)




print(type(d))

Student={

    "name":"Ronit",
    "age":24,
    "grade":"A"
}
index=hash("name")%2
print(index)

index=hash("age")%2
print(index)

index=hash("grade")%2
print(index)

Student.get("name")
print(Student.get("name"))

my_dict_int_key={1:"one",200:"two hundred",0:"zero"}
my_dict_float_key={3.14: "Pi",9.81:"Gravity",2.718:"Euler's number"}
my_dict_bool_key={True:"It's True",False:"It's False"}
my_dict_tuple_key={
    (34.0522, -118.2437): "Los Angeles",
    (40.7128, -74.0060): "New York"
}
print(my_dict_int_key.get(200))
print(my_dict_float_key.get(3.14))
print(my_dict_bool_key.get(True))
print(my_dict_tuple_key.get((34.0522, -118.2437)))

print(dict(a=1,b=2))

# ACCESSING DICTIONARY ELEMENTS
# Using square Brackets[]
# Using get() Method
person={'name':'Alice','age':24}
print(person['name'])
print(person.get('age'))
print(person.get('hello'))  # Will give none

students={'Alice':78,'Arisu':90,'Usagi':99}
key=input()
print(students.get(key,"Not Found"))
if key in students:
    print(students[key])
else:
    print("Not Found")

# MODIFYING DICTIONARIES
person={"name":"Artemis","age":24}
person['age']=26
person['city']="New York"
print(person)
del person['city']
print(person)

print(person.pop('name'))  # pops the desired element
print(person.pop('something','NA')) # error if not found else use fallback
person.clear()
print(person)

person={"name":"Artemis","age":24}
person.popitem()  # pop item removes last one
print(person)

# dict1.update(dict2)
#dict1: the dictionary to be updated.
#dict2: The dictionary (or key-value iterable)providing updates.

profile={'name':'Vostrok','age':24}
updates={'age':31,'city':'Las Vegas'}
profile.update(updates)
print(profile)

profile={'name':'Rexonic'}
profile.update([('age',12),['city','New Zealand']])
print(profile)

profile.update(country='something',rfrfr='Phoenix')
print(profile)

# DICTIONARY OPERATIONS
student ={"name":"Jackal","age":24,"grade":"C"}
print("name"in student)  # returns boolean value
print(len(student))

for i in student:
    print(student[i]) # returns value of dictionary
    print(i)  # returns the key of dictionary
    print(i,student[i])  # returns a complete pair of keys and value

data={"a":1,"b":2}
print(1 in data)

data={
    "id":101,
    "info":{
         "name":"Jack",
         "city":"New York"
     }
}

print(data.get("info"))

# DICTIONARY METHODS - keys(), values(), items()
student={"name":"Christie","age":21,"grade":"A"}
keys=student.keys() # Similar to set
student["city"]='Dehradun'
print(keys)  # Live Reflection of dictionary changes
print(student.values())
print(student.items())

# ITERATION THROUGH DICTIONARY
person={"name":"Taylor","age":27,"city":"San francisco"}
for i in person:
    print(person[i]) # values

for i in person:
    print(i)  # keys

for key, value in person.items():
    print(f"{key}: {value}")  # Unpacking of Dictionary

data={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6}

# Incorrect way
'''for k in data:
    if data[k]%2 ==0:
        del data[k]
print(data)'''

# Correct way : Iterating over a copy
for k in list(data.keys()):
    if data[k]%2 ==0:
        del data[k]
print(data)

# Complex Data Structures
students={
     "101":{"name":"Ronit","age":24,"grade":"A"},
     "102":{"name":"Rahul","age":22,"grade":"B"},
     "103":{"name":"Sam","age":26,"grade":"C"}
 }
print(students["101"]["grade"])

for  roll,details in students.items():
    for k,v in details.items():
        print(f"{k}: {v}")


profile={
    "username":"Jade",
    "details": {
        "name":"Jack Madelena",
        "city":"New York",
        "age": 24
    }
}

# MERGING DICTIONARIES
a={'a':1}
b={'b':2,'a':12}

a=b|a
print(a)

# print(a.get('c','NA'))
print(a.setdefault('c',123))
print(a)
# Retrieve the value of a key if it exists

# DICTIONARY COMPREHENSION
# {key_expression: value_expression for item in iterable if condition}
res={}
for i in range(6):
    res[i]=i**2    # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(res)

ses={}
for i in range(1,11):
    if(i%2==0):
        ses[i]=i**2
    else:
        ses[i]=i**3
print(ses)

res={i:i**2 if i%2==0 else i**3 for i in range(1,11)}
print(res)

res={i: i**2 for i in range(1,11) if i%2==0}
print(res)

students=[("Alice",90),("Bob",90),("Charlie",89)]
res={i:j for(i,j) in students}
print(res)
print(students)

original={'a':1,'b':2,'c':3}
res={j:i for(i,j) in original.items()}
print(res)

# Create a Multiplication table from 1 to 5 using nested dictionary comprehension
pes={}

for i in range(1,6):
    table={}
    for j in range(1,11):
      table[j]=i*j
    pes[i]=table

for i in pes:
    print(f"{i}: {pes[i]}")

# Same using comprehension
res={i:{j:i*j for j in range(1,11)} for i in range(1,6)}
for i in res:
    print(f"{i}: {res[i]}")

# Shallow and Deep Copy
# Shalllow copy
student={
    "name": "Akshit",
    "marks": [89.56,92]
}
another_student=student.copy()
student["marks"].append(99)
print(student)
print(another_student)

# Deep copy
import copy
student={
    "name": "Rahul",
    "marks": [89,78,92]
}
deep_copy_student=copy.deepcopy(student)
deep_copy_student["marks"].append(100)
print(student["marks"])
print(deep_copy_student["marks"])
