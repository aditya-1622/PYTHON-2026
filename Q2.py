# find square root of a number:

# Solution 1: using exponent operator:

num = 64
num1= int(input("Enter a number here:"))

sr = num**(1/2) #we can also use sr = 0.5
print("the square root of given number is", sr)

# Method 2 (Using math module)

import math
num = int(input("Enter a number here:",))
sr = math.sqrt(num)
print("Square root of the given number is", sr)