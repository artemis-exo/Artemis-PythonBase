# print("Hello Vro")
#
# a=int(input("Enter a number"))
# for i in range(2,a):
#     if(a%i==0):
#         print("Not a prime")
#         break
# else:
#   print("Prime")


# b=int(input("Enter a number"))
# fact=1
# for i in range(1,b+1):
#     fact=fact*i
# print(f"The factorial of {b} is {fact}")
#
# i=1
# fact=1
#
# while i<=b:
#     fact=fact*i
#     i+=1
# print(f"The factorial of {b} is {fact}")
#
# c=int(input("Enter a number"))
#
# rev=0
# while c>0:
#     rev=rev*10+(c%10)
#     c=c//10 # to avoid floating
# print(rev)
#
# for i in range(1,6):
#     if(i==5):
#         continue
#     for j in range(1,11):
#         if j==7:
#             break
#         print(f"{i}X{j}={i*j}",end=" ")
#     print()
#
# def prime(n):
#     for i in range(2,n):
#         if(n%i==0):
#             print("Not a prime")
#             break
#     else:
#       print("Prime")
#
# a=int(input("Enter a number"))
# prime(a)
#
# def prime(n):
#     for i in range(2,n):
#         if(n%i==0):
#             print("Not a prime")

import numpy as np
from numpy.ma.core import concatenate

arr=np.array([1,"MCA First sem"])
print(arr)
print(type(arr))
print(arr.ndim)

arr1=np.array(10)
print(arr1)
print(arr1.ndim)

# 2D array

import numpy as np
arr=np.array([[1,"MCA First sem",2],[3,4,5],[6,7,8]])
print(arr)

print(arr.ndim)

arr=np.array([1,2,3,4,5])
x=arr.copy()
arr[0]=44
print(arr)
print(x)

# View - sharing same memory location
arr=np.array([1,2])
x=arr.view()
arr[0]=44
print(arr)
print(id(arr))
print(x)
print(id(x))

# Numpy array Shape
# Returns the tuple with each

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr.shape)

arr=np.array([1,2,3,4,5],ndmin=5)


# Numpty arr and List concatenate
# list=[12,3,4,5]
# arr1=np.array([1,2,3,4,5])
# concatenate(list,arr)


#Pandas
import pandas as pd
print(pd.__version__)

data={
    "Name":["Vedaant","Rohit","Vedant"],
    "Marks": [90,85,92]
}
df=pd.DataFrame(data)
print(df)

import matplotlib.pyplot as plt
plt.plot([1,2,3],[4,5,6])
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
sns.lineplot(x=[1,2,3],y=[3,1,4])
plt.show()

from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier

iris=datasets.load_iris()

x=iris.data
y=iris.target

model=DecisionTreeClassifier()

model.fit(x,y)

pred=model.predict([x[0]])
print("Prediction:",pred)

import tensorflow as tf
print("TensorFlow version:",tf.__version__)




