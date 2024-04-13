#This file purely exists for development purposes such that I can test methods and functions as they are implemented.

from linalgebralib import LinAlgLib as la

A = la.columnVector([3,4])
B = la.columnVector([-4,3])
print(la.angle(A,B))

#TODO: 

#Fixed matrix multiplication method. Added support for multiplication of matrices and vectors of appropriate dimensions and vice versa.
#Fixed determinant method such that it can handle matrices where row swaps are required, and keeps track of row swaps such that an accurate value for the determinant is returned.
#Implemented transpose method for vectors. 
#Implemented method to compute the inverse of invertible matrices. 
#Implemented method to compute the dot product of two vectors.
#Implemented method to compute the angle between two vectors.
