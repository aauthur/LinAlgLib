# LinAlgLib

### About the Project

This library aims to offer user-friendly functionality for several important concepts from linear algebra, from basic matrix algebra to more complex operations like computing the null space of a matrix. LinAlgLib will be uploaded to PyPi as soon as I finish implementing the operations it should be able to handle. Until then the code will be available from this repository, and the documentation will be updated with each push to reflect what has currently been implemented. 

### Purpose

Although numpy and scipy already support most if not all of the computations that can be handled by this library, I produced this library mainly as an exercise. As far as its utility goes, it is my goal to make this library more intuitive for laypeople in math and science fields to be able to jump in and start running through calculations immediately without having to review much documentation.

### Technologies

[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

This project was built for Python, with the ultimate aim of contributing to other machine learning libraries.

# Documentation
The following documents everything presently supported by linalglib.

# Row Vectors
rowVector objects allow users to create Row Vectors for the purposes of matrix initialization, or for uncommon applications requiring row vectors.

## Instantiation
```
r = rowVector(contents=[], size=0)
```

Contents should be passed as a list of values to appear in the row vector. If the contents field is passed, size is unnecessary. The size attribute simply denotes the number of columns in the row vector, and will automatically be matched to whatever is passed in the contents field. 

The size attribute is left as an option for instantiation in case the user would like to instantiate a zero vector of a specified dimension, which the user can do by passing a parameter to the size field, but not to the contents field.

Examples
```
r1 = rowVector([1,2,3])
r2 = rowVector(size=3)
```

Here print(r2) will output [0,0,0] as it is initialized as a zero vector with three columns.

## Methods
### Adding 
Two vow vectors, or a row vector and a matrix of equal dimension, can be added together. 

Examples
```
row_vector3 = row_vector1 + row_vector2

new_row_vector = 1x3row_vector + 1x3matrix

new_1x3matrix = 1x3matrix + 1x3row_vector
```
Note: As illustrated by examples 2 and 3, the type of the resultant object after vector addition is dependent on which type comes first in the operation. If the user wants the result as a matrix, they should follow the order in example 3. If instead, the user wants a row vector as their result, they should follow the order in example 2.

### Subtracting
Two row vectors, or a row vector and a matrix of equal dimension, can be subtracted from one another. 

Examples
```
row_vector3 = row_vector1 - row_vector2

new_row_vector = 1x3row_vector - 1x3matrix

new_1x3matrix = 1x3matrix - 1x3row_vector
```
Note: As illustrated by examples 2 and 3, the type of the resultant object after vector subtraction is dependent on which type comes first in the operation. If the user wants the result as a matrix, they should follow the order in example 3. If instead, the user wants a row vector as their result, they should follow the order in example 2.

### Scalar Multiplication
Row vectors can be scaled by floats and integers.

Example
```
a1 = rowVector([1,2,3])  
print(a1*3)
```
This will output [3,6,9]

# Column Vectors
columnVector objects allow users to create column vectors. Column vectors can be used on their own for applications involving them, or a list of column vectors can be used in order to instantiate a matrix.

## Instantiation
```
v = columnVector(contents=[], size=0)
```

Contents should be passed as a list of values to appear in the row vector. If the contents field is passed, size is unnecessary. The size attribute simply denotes the number of columns in the column vector, and will automatically be matched to whatever is passed in the contents field. 

The size attribute is left as an option for instantiation in case the user would like to instantiate a zero vector of a specified dimension, which the user can do by passing a parameter to the size field, but not to the contents field.

Examples
```
v1 = columnVector([1,2,3])
v2 = columnVector(size=3)
```

Here print(r2) will output [0,0,0]**T as it is initialized as a zero vector in R<sup>3</sup>.

## Methods
### Adding 
Two column vectors, or a column vector and a matrix of equal dimension, can be added together. 

Examples
```
column_vector3 = column_vector1 + column_vector2

new_column_vector = 3x1column_vector + 3x1matrix

new_matrix = 3x1matrix + 3x1column_vector
```
Note: As illustrated by examples 2 and 3, the type of the resultant object after vector addition is dependent on which type comes first in the operation. If the user wants the result as a matrix, they should follow the order in example 3. If instead, the user wants a column vector as their result, they should follow the order in example 2.

### Subtracting
Two column vectors, or a column vector and a matrix of equal dimension, can be subtracted from one another. 

Examples
```
column_vector3 = column_vector1 - column_vector2

new_column_vector = 3x1column_vector - 3x1matrix

new_matrix = 3x1matrix - 3x1column_vector
```
Note: As illustrated by examples 2 and 3, the type of the resultant object after vector subtraction is dependent on which type comes first in the operation. If the user wants the result as a matrix, they should follow the order in example 3. If instead, the user wants a column vector as their result, they should follow the order in example 2.

### Scalar Multiplication
Column vectors can be scaled by floats and integers.

Example
```
v = columnVector([1,2,3])  
print(v*3)
```
This will output [3,6,9]**T

# Matrices
Matrix objects allow users to create matrices. Matrices are associated with several methods listed below.

## Instantiation
```
A = Matrix(contents=[], size=(0,0))
```

Matrices can be instantiated from a list of lists, a list of row vectors, or a list of column vectors. The size attribute will automatically be assigned based on the contents if they are given. If the contents parameter is not given, but the size parameter is, then an (m x n) zero matrix will be generated with size=(m,n).

Examples
```
c1 = rowVector([1,2,3])
c2 = rowVector([4,5,6])
c3 = rowVector([7,8,9])
b1 = columnVector([1,4,7])
b2 = columnVector([2,5,8])
b3 = columnVector([3,6,9])
A = Matrix(content=[[1,2,3],[4,5,6],[7,8,9]])
B = Matrix(content=[b1,b2,b3])
C = Matrix(content=[c1,c2,c3])
D = Matrix(size=(2,3))

```

Here A, B, C are all the same 3x3 matrix. print(D) will output the following\
[0,0,0]\
[0,0,0]

## Methods
### Adding 
Two matrices of the same dimension can be added together according to the rules of matrix algebra.

Example
```
new_matrix = 3x3matrix_a + 3x3matrix_b
```
### Subtracting
Two matrices of the same dimension can be subtracted from one another according to the rules of matrix algebra.

Example
```
new_matrix = 3x3matrix_a - 3x3matrix_b
```

### Matrix Multiplication
As in matrix algebra, (m x n) matrices can multiply on the left with (n x l) matrices, where l is any positive integer. They can also be scaled by integers or floating point numbers.

Example
```
A = 2x2matrix * 2x3matrix
B = 2*Matrix(content=[[1,1],[1,1]])
```
A will be a 2x3 matrix, and B will be the following matrix\
[2,2]\
[2,2]

### Row Operations
All 3 elementary row operations are supported by this library by the following methods.

1. row_swap(r1, r2)
2. row_scale(r, c)
3. row_addition(r, rc, c=1)

The row_swap method swaps two rows of a matrix by their indices r1, and r2. The row_scale method scales a given row by an integer or floating point number, and the row_addition method adds a scaled (optional) copy of the row indexed by rc to the row indexed by r. When c is specified, rc will be scaled by that integer or floating point number prior to being added to row r. 

These methods will likely not be utilized by the user, and primarily exist for the purposes of other computations such as the row-echelon and reduced row-echelon forms of the matrix. 

### Transpose
`A.transpose()` will return a copy of the transpose of matrix A, with A's rows forming the columns of its transpose.

Example
```
A = Matrix(content=([1,2],[3,4])
print(A.transpose())
```
This will return\
[1,3]\
[2,4]

### Row-Echelon Form
`A.ref()` will return a copy of matrix A in row-echelon form. It is useful to keep this separate from reduced row-echelon form for computing the determinant.

Example
```
A = Matrix(content=([1,2],[3,4])
print(A.ref())
```
This will return\
[1,2]\
[0,-2]

### Reduced Row-Echelon Form
`A.rref()` will return a copy of matrix A in reduced row-echelon form.

Example
```
A = Matrix(content=([1,2],[3,4])
print(A.rref())
```
This will return\
[1,0]\
[0,1]

### Determinant
`A.det()` will return the value of the determinant of matrix A.

Example
```
A = Matrix(content=([1,2],[3,4])
print(A.det())
```
This will return\
-2

### Row Space
`A.row_space()` will return a set of the basis vectors for the row space of matrix A. It is important to note that the vectors in this basis are row vectors.

Example
```
A = Matrix(content=([1,2],[3,4])
print(A.row_space())
```
This will return\
{(1,0),(0,1)}

### Column Space
`A.column_space()` will return a set of the basis vectors for the column space of matrix A. It is important to note that the vectors in this basis are column vectors.

Example
```
A = Matrix(content=([1,2],[3,4])
print(A.column_space())
```
This will return\
{(1,2), (3,4)}

