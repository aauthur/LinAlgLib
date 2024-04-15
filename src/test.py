#This file purely exists for development purposes such that I can test methods and functions as they are implemented.

from linalgebralib import LinAlgLib as la

A = la.columnVector([3,4])
B = la.columnVector([-4,3])
print(la.angle(A,B))

#TODO: Implement vector projections, unit vectors, cross product.