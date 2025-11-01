# Python integers have unlimited precision
a= 2362453453453746378463877
print(type(a))

salary=10_00_000
print(salary)

binary_num=0b101010  # Stores binary
print(bin(10))
print(type(binary_num))
print(binary_num)  # Output 42
hex_num=0x2A
print(hex_num)

a=10
b=6
print(f"Addition: {a+b}")
print(f"Subtraction: {a-b}")
print(f"Multiplication: {a*b}")
print(f"Regular Division: {a/b}")  # 1.6666666666666667
print(f"Integer Division: {a//b}")
print(f"Pow: {a**b}")
print(f"Modulus: {a%b}")
print(f"Negation of{a}={-a}")  # Corresponding Negative
print(f"Absolute value of {b} - {a} ={abs(b-a)}")  #Absolute value

res=2+3*4
print(res)

# Precedence order --> ()> ** > *,/,//,% > +,-

result=10-2**3//2+7
print(result)

# BitWise Operators
x=10  # 1010 in binary
y=6   # 0110 in binary
      # 0010

#BitWise AND &
bitwise_a=x&y
print(f"{x} & {y} = {bitwise_a}")

#Bitwise OR ||
x=10  # 1010 in binary
y=6   # 0110 in binary
      # 1110
bitwise_or=x|y
print(f"{x} | {y} = {bitwise_or}")

#Bitwise XOR ^ When bits are different then 1 else 0
x=10  # 1010 in binary
y=6   # 0110 in binary
      # 1100
biwise_xor=x^y
print(f"{x} ^ {y} = {biwise_xor}")

#Bitwise NOT ~
x=10  # only one operand in this
#binary  - 1010
 #         0101

bitwise_no=~x
print(f"~{x}={bitwise_no}")

#Left Shift <<
x=10
#binary   1010
       #  10100
left_shift=x <<1
print(f"{x} << = {left_shift}")

#Right Shift
x=10
#binary   1010
#          101
right_shift=x >> 1
print(f"{x} >> = {right_shift}")

#Questions
print(10//3)  #3
print(10.0//3)  # 3.0
print(-10//3)   # -4
print(10//-3)   # -4

# Floor divion - Returns largest integer less than or equal to the exact division

# Assignment operator
x=1
name="Vedaant"
a,b=4,6

# * User input
x=input()
y=input()

print(x+y)
print(type(x+y))   # It acts as a string

# We have to enter the values
x=int(input("Please input ki value daldo"))
y=int(input("KARO PLEASE"))
print(type(x),type(y))

#Swapping Elements
x,y=y,x
print(x,y)

#Shortcuts
salary =11
salary **=2
print(salary)

msg="Hello"
msg+="World"
print(msg)



