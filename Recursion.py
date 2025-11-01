'''
Recursion is when a function solves a big problem by solving
 a smaller version of the same problem and uses that result to finish the job
'''

def sum_rec(n):
    if n == 1:
        return 1
    return n + sum_rec(n-1)

print(sum_rec(5))

# Factorial

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

print(factorial(5))

import sys
print(sys.getrecursionlimit())

'''
Avoid recursion when:
1. Problem size may exceed recursion depth(e.g. factorial of 10,000).
2. Performance is critical(since recursion adds overhead or function calls)
3. An iterative solution is clear and simpler
'''

'''
Use recursion when:
1. Problem has a natural recursive definition(trees, backtracking)
2. Code readability and clarity outweigh performance concerns
'''

# FIBONACCI SERIES
# 0,1,1,2,3,5,8,13,21,34, ....

def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib(n-1) + fib(n-2)

print(fib(10))

# Backward Counting
def count_down(n):
    if n==0:
        return
    print(n)
    count_down(n-1)

count_down(5)

# Forward Counting
def count_down1(n):
    if n==0:
        return
    count_down1(n-1)
    print(n)

count_down1(5)