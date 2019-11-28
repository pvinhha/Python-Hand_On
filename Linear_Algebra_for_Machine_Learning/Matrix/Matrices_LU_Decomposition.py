# Matrix Factorization
# Matrix LU decomposition
# The LU decomposition is for square matrices and decomposes a matrix into L and U components. 
# A = L . U

from numpy import array
from scipy.linalg import lu
# define a square matrix
A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
# LU decomposition
# Where A is the square matrix that we wish to decompose, 
# L is the lower triangle matrix and U is the upper triangle matrix. 
# A variation of this decomposition that is numerically more stable to solve 
# in practice is called the LUP decomposition, or the LU decomposition with partial pivoting.
P, L, U = lu(A)
print(P)
print(L)
print(U)
# A = L . U . P
# The rows of the parent matrix are re-ordered to simplify the decomposition process and the additional 
# P matrix specifies a way to permute the result or return the result to the original order. There are also 
# other variations of the LU.

# reconstruct
B = P.dot(L).dot(U)
print(B)
