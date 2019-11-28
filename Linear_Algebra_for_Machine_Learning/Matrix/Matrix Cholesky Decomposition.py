# Cholesky decomposition. Return the Cholesky decomposition, 
# L * L.H, of the square matrix a, where L is lower-triangular 
# and.H is the conjugate transpose operator 
# (which is the ordinary transpose if a is real-valued). 
# a must be Hermitian (symmetric if real-valued) and positive-definite. 
# Only L is actually returned.

from numpy import array
from scipy.linalg import cholesky
# define a symmetric matrix
A = array([[6, 3, 4, 8], [3, 6, 5, 1], [4, 5, 10, 7], [8, 1, 7, 25]])
print("Hermitian (symmetric matrix) A: ")
print(A)
# QR decomposition
# Where A is the square matrix that we wish to decompose, 
# Calculate the decomposition A = L * L.H.
L = cholesky(A, lower=True)
print("Low left matrix L: ")
print(L)

# The upper can be calculated as
print("Upper right matrix U: ")
U = cholesky(A, lower=False)
print(U)

# reconstruct:
B = L.dot(U)
print("Reconstruct from L and U: ")
print(B)
