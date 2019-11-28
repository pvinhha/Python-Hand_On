# Matrix Factorization
# Matrix QR decomposition
# A = Q. R

from numpy import array
from scipy.linalg import qr
# define a square matrix
A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
# QR decomposition
# Where A is the square matrix that we wish to decompose, 
# Calculate the decomposition A = Q R where Q is unitary/orthogonal and R upper triangular.
Q, R = qr(A)
print(Q)
print(R)

# Reconstruct from Q and R matrices to get the original matrix
B = Q.dot(R)
print(B)
