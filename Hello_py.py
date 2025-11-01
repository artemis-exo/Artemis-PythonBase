print("Hello Vro")

a=int(input("Enter a number"))
for i in range(2,a):
    if(a%i==0):
        print("Not a prime")
        break
else:
  print("Prime")


b=int(input("Enter a number"))
fact=1
for i in range(1,b+1):
    fact=fact*i
print(f"The factorial of {b} is {fact}")

i=1
fact=1

while i<=b:
    fact=fact*i
    i+=1
print(f"The factorial of {b} is {fact}")

c=int(input("Enter a number"))

rev=0
while c>0:
    rev=rev*10+(c%10)
    c=c//10 # to avoid floating
print(rev)

for i in range(1,6):
    if(i==5):
        continue
    for j in range(1,11):
        if j==7:
            break
        print(f"{i}X{j}={i*j}",end=" ")
    print()

def prime(n):
    for i in range(2,n):
        if(n%i==0):
            print("Not a prime")
            break
    else:
      print("Prime")

a=int(input("Enter a number"))
prime(a)

import numpy as np
def prime(n):
    for i in range(2,n):
        if(n%i==0):
            print("Not a prime")



