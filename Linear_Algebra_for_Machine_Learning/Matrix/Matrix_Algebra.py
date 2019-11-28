# A matrix is a two-dimensional array of scalars with one or more columns and one or more rows.

# The notation for a matrix is often an uppercase letter, such as A, and entries are referred to 
# by their two-dimensional subscript of row (i) and column (j), such as aij. For example: 

# A = ((a11, a12), (a21, a22), (a31, a32))
# Defining a Matrix
# We can represent a matrix in Python using a two-dimensional NumPy array.

# A NumPy array can be constructed given a list of lists. For example, below is a 2 row, 3 column matrix. 

# create matrix
from numpy import array
A = array([[1, 2, 3], [4, 5, 6]])
print("Matrix A of 2x3: ")
print(A)
# Matrix Addition
# Two matrices with the same dimensions can be added together to create a new third matrix. 

# C = A + B
# The scalar elements in the resulting matrix are calculated as the addition of the elements in each of the matrices being added.

# We can implement this in python using the plus operator directly on the two NumPy arrays. 

# add matrices
B = array([[1, 2, 3], [4, 5, 6]])
print("Matrix B of 2x3: ")
print(B)

C = A + B
print("New Matrix C = A + B: ")
print(C)
# Matrix Dot Product
# Matrix multiplication, also called the matrix dot product is more complicated than the previous operations 
# and involves a rule as not all matrices can be multiplied together.

# The rule for matrix multiplication is as follows: 
# The number of columns (n) in the first matrix (A) must equal the number of rows (m) in the second matrix (B).

# For example, matrix A has the dimensions m rows and n columns 
# and matrix B has the dimensions n rows and k columns. The n columns in A and n rows b are equal. 
# The result is a new matrix with m rows and k columns. 

# C(m,k) = A(m,n) * B(n,k)
# The intuition for the matrix multiplication is that we are calculating the dot product between 
# each row in matrix A with each column in matrix B. For example, we can step down rows of 
# column A and multiply each with column 1 in B to give the scalar values in column 1 of C.

# The matrix multiplication operation can be implemented in NumPy using the dot() function. 

# matrix dot product
A = array([[1, 2], [3, 4], [5, 6]])
print("Matrix A of 3x2: ")
print(A)
B = array([[1, 2], [3, 4]])
print("Matrix B of 2x2: ")
print(B)
C = A.dot(B)
print("Resultant Matrix C = dot(A,B) of 3x2: ")
print(C)

# Define new 3x3 square matrices
A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = 2 * A
print("Matrix A of 3x3: ")
print(A)
print("Matrix B of 3x3: ")
print(B)
# Matrix subtraction
C = B - A
print("New Matrix C = B - A: ")
print(C)

# Matrix division
C = B / A
print("New Matrix C = B / A: ")
print(C)

# Matrix Hadamard product is the elementwise multiplication and require 2 matices with the same dimension
C = A * B
print("New Matrix C = A * B: ")
print(C)

# Vector Matrix multiplication is a dot product and must have the same dimension requirement for A columns = V rows
# define Vector matrix of 3x1
V = array([[2],[4],[8]])
print("Vector matrix of 3x1: ")
print(V)

# Vector matrix multiplication
D = A.dot(V)
print("Resultant  D = dot(A,V):")
print(D)