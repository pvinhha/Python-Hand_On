# Types of matrices and matrix operations.
import numpy as np
from numpy import array, linalg
from numpy.linalg import inv, det


# Transpose
# A defined matrix can be transposed, which creates a new matrix with the number of columns and rows flipped.
# This is denoted by the superscript “^T” next to the matrix
# Define new 3x3 square matrices
A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
C = A.T
print("Matrix A of 3x3: ")
print(A)

print("Resultant Matrix C = A^T of 3x3: ")
print(C)

# Inversion
# The operation of inverting a matrix is indicated by a -1 superscript next to the matrix; 
# for example, A^-1. The result of the operation is referred to as the inverse of the original matrix; 
# for example, B is the inverse of A.

# define a square matrix
A = array([[1.0, 2.0], [3.0, 4.0]])
print(A)
B = inv(A)
print("Resultant Matrix B = A^-1 of 3x3: ")
print(B)

# Square Matrix
# A square matrix is a matrix where the number of rows (n) equals the number of columns (m). 

# n = m
# The square matrix is contrasted with the rectangular matrix where the number of rows and columns are not equal.

# Symmetric Matrix
# A symmetric matrix is a type of square matrix where the top-right triangle is the same as the bottom-left triangle.

# To be symmetric, the axis of symmetry is always the main diagonal of the matrix, from the top left to the bottom right.

# A symmetric matrix is always square and equal to its own transpose. 

# M = M^T
M = array([[1, 4, 7], [4, 5, 8], [7, 8, 9]])
print("Square matrix M: ")
print(M)
M = M.T
print("Symmetrical matrix M: ")
print(M)

# Triangular Matrix
# A triangular matrix is a type of square matrix that has all values in the upper-right or lower-left of the matrix with the remaining elements filled with zero values.

# A triangular matrix with values only above the main diagonal is called an upper triangular matrix. Whereas, a triangular matrix with values only below the main diagonal is called a lower triangular matrix.
T = np.tri(4,4,0)
print("Triangle matrix T: ")
print(T)

# Diagonal Matrix
# A diagonal matrix is one where values outside of the main diagonal have a zero value, where the main diagonal is taken from the top left of the matrix to the bottom right.

# A diagonal matrix is often denoted with the variable D and may be represented as a full matrix or as a vector of values on the main diagonal.
D = np.diag((-2,-1,1,2))
print("Diagonal matrix D: ")
print(D)

# Get Hadamard product from T and D
H = T * D
if(det(H) >= det(T)*det(D)):
    print("Determinant Hadamard elementwise multiplication works as expected")
else:
    print("Determinant of Hadamard product doesn't work!")

print("Matrix H")
print(H)

# Matrix rank the result to get the number of singular values diagonal elements
R = linalg.matrix_rank(H)
print("Matrix range R for H:")
print(R)

# Trace to get the sum value of the SVD elements
TR = np.trace(H)
print("Matrix trace TR for H:")
print(TR)

