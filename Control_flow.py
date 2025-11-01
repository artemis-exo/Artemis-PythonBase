print("Good Morning")
name="Kyla"
print(f"Hello {name}")
print("Welcome to Python programming")

'''
1. making decisions
2. repeating actions
3. jumping to different parts of the program
'''
age=int(input("Enter your age: "))
if age>=18:
    print("You are an Adult ")
    print("I mean you are an Adult ")  # In python there is a space intendation which executes the loop
print("Come outside the block") # this will if the loop will be false or true beacuse it is not the part of if Block

temp= int(input("Enter Temperature: "))
is_raining=bool(input("Leave Empty if raining else Type anything"))  #True
print(is_raining)
if temp<=10 and is_raining:
    print("Wera jacket ")
print("And don't forget your boots!")
print("Prince of nail")
print("Have a nice day")

name="b"  # After entering b it becomes True
if name:
    print(name)
# Example
cool=5
is_snowing=True

if cool<10:    # If this becomes false the snowing condition will not execute
    print("It's freezing! ")
    print("Wear a heavy coat.")
    if is_snowing:    # This condition is under temp
        print("And don't forget your boots!")
print("Have a nice day")     # This line will always print


# Example
money=600
is_popcorn=True
if money>=400:
    print("Let's watch a movie ")
    if(is_popcorn):
        print("Let's have some popcorn!")

# Example
score=89
if score>=90:
    print("EXCELLENT")
    print("Keep up the good work")

if score<60:
    pass  # If we want to pass this condition
print("Hardwork")

# ELSE
score =76
if score<=33:
    print("FAIL")
else:
    print("PASS")

age=18
password=input("Enter your password: ")
if age>=18:
    if len(password)>=8:
        print("Valid password")
    else:
        print("Invalid password")
else:
    print("Your age is too less")

# EIF(else-if)

score =66
if score>=90:
    GRADE="A"
elif score>=80:
    GRADE="B"
elif score>=70:
    GRADE="C"
elif score>=60:
    GRADE="D"
else:
    print("Fail have to do hardwork")
print(f"Your grade is {GRADE}")

#Example
number=int(input("Enter a number: "))
if 0<number<=9:
    print("Positive single digit number")
elif number<=0:
    print("Negative or Zero ")
elif number>9:
    print("High number")

# Example
# Else if executes only one condition
has_fever=True
has_cough=True
has_rash=True
if has_cough:
    print("Take cough syrup")
if has_fever:
    print("Take fever medication")
if has_rash:
    print("Apply anti-itch cream.")

#Example
a=96
if a==6 or a==7 or a==9:
    print("Lucky")
else:
    print("Unlucky")

# same using list
a=96
if a in [6,7,9]:
    print("Lucky")
else:
    print("Unlucky")

# TERNERY OPERATOR
age=20
status="adult" if age>=18 else "minor"
print(status)

#Example
number =16
divisor=7
result =number/divisor if divisor!=0 else "Cannot be divide by zero"
print(result)

#Examaple
operation =input("sub or add ?")
a,b=5,7
result=a+b if operation=="add" else a-b if operation=="sub" else "Unknown operation"
print(result)

i=0
while i<5:
    if(i==3):
        i+=1
        continue
    print(i)
    i=i+1