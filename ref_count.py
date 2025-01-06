import sys


a = []

b = a  #Shared mutable objects
d = b
h = b
l = d
m = l
p = h
z = a
print(sys.getrefcount(a))

#Object is eligible for garbage collection when reference count is 0