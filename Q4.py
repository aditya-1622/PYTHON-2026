# program to swap two variables.

# Method 1: using third var:
x = 13
y = 12
temp = x
print("The value of temp var is",temp)

x = y
print("The value of x is",x)

y = temp 
print("The value of y is", y)

# Method 2: without using third var:
x = 12
y = 13

x, y = y, x
print("The value of x is", x)
print("The value of y is", y)