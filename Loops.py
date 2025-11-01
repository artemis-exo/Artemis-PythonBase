print("Hello Vro")

# WHILE LOOP
'''
while condition:
    # code block to be executed 
'''

x=1
while x<=10:
    print("Hello Vro",x)
    x=x+1
    if x==4:
        break

x=1
while True:
    print("OK")
    x=x+1
    if x==4:
        break

x=10
while x>0:
    print(x)
    x-=1

# FOR LOOP

'''
for variable in sequence:
    print(variable)
    # Code block (loop body)
'''
fruits=["apple","orange","banana"]
print(fruits[1])

for fruit in fruits:
    print(fruit)

name="Vedaant"
for vec in name:
    print(vec.upper())

# Range
# Generate a sequence of numbers
# range(stop)               Starts from 0 to stop- 1
# range(start,stop)         Starts start to stop-1
# range(start,stop,step)    Start from start to stop-1, incremented
#   It does not create a list in memory (Unless explicitly converted), but rather returns a range object that produces numbers on demand

print(list(range(10)))

for i in range(5):
    print("Hello world",i)

for i in range(1,5):
    print("Hello Asia",i)

for i in range(1,6,2):
    print("Hello uni",i)

#Range as Index
fruits=["apple","orange","banana","mango"]
for i in range(len(fruits) -1,-1,-1):
    print(fruits[i])

fruits=["apple","orange","banana","mango"]
i=0
for fruit in fruits:
    print(fruit[i])
    i+=1
# Enumerate
print(list(enumerate((fruits))))

for fruit in enumerate(fruits):
    print(fruit)

for index, fruit in enumerate(fruits):
    print(fruits[index])

# Break - Immediately exits the loop,regardless of the loop condition
for number in range(10):
    if number==5:
        break
    print(number)

# Continue - Skips the current iteration and moves to the next one.
for number in range(10):
    if number==5:
        continue
    print(number)

# Pass - It is like a Do-nothing placeholder. The loop does nothing when pass is hit
for number in range(10):
    if number==5:
        pass
    print(number)

# Let's try odd and Even till 20
for number in range(1,21):
    if number % 2==0:
        print(f"{number} is even")
       # print(i,"Even") - we can also do it like this
    else:
        print(f"{number} is odd")

# Let's check whether a Entered number is Prime or not
x=int(input("Enter a number"))
count=0
for i in range(1,x+1):
    if x%i==0:
        count+=1
if count==2:
     print("Yes the number is Prime")
else:
     print("No the number is not prime")

# for and while loops can have an optional else
# The else block executes after the loop finishes normally
# but not if the loop is terminated early with a break
'''
for item in seqence:
    #Loop Body
    if some_condition:
        break
else:
     # Runs only if the loop was not broken

'''

# Finding even numbers in list
nums=[1,3,5,7,9]
for num in nums:
    if num%2==0:
        print("Even number found",num)
        break
else:
    print("No even number found")

# Nested Loops
'''
*
**
***
****
*****
'''
for i in range(1,6):
    stars=""
    for j in range(i):
        stars+="*"
    print(stars)

print("This is separator")

'''
*****
*****
*****
*****
'''
for i in range(1,5):
    st=""
    for j in range(5):
        st+="*"
    print(st)





