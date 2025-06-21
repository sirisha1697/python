"""
Logical Operators are used to perform logical Operations
The Operators are 
Logical OR--If one of the condition is True then its going to Return the True
Logical AND-- If Both the conditions are True then its going to return the True
Logical NOT-- It just negotiates the condition
"""
a = 23
b = 30
c = a<b and b>a #t and t -- t
print(c)#True

d = 40
e = 45
f = d>e or e>d # f or t --t 
print(f)#true

a = 1
print(not(a)) #FALSE 

a = 0
print(not(a)) #True