from numpy import array
import numpy as np
from scipy.linalg import eigvals # for non-symmetrical matrix, return only W
from scipy.linalg import eigh   # for symmetrical matrix, return W and Vr
from scipy.linalg import eig    # for generic array, return W and Vr

# define a square matrix
A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Square matrix A: ")
print(A)

# Eigen decomposition
# Where A is the square matrix that we wish to decompose, 
# Calculate the decompositions of eigenvalue W.
W = eigvals(A)
print("Eigen value W: ")
print(W)

# define a symmetric matrix
A = array([[6, 3, 4, 8], [3, 6, 5, 1], [4, 5, 10, 7], [8, 1, 7, 25]])
print("Hermitian (symmetric matrix) A: ")
print(A)

# The eigenvalues W, each repeated according to its multiplicity. 
# The eigenvalues are not necessarily ordered. The resulting array will be of complex type, 
# unless the imaginary part is zero in which case it will be cast to a real type. 
# When a is real the resulting eigenvalues will be real (0 imaginary part) or occur in conjugate pairs

# The normalized (unit “length”) eigenvectors V, such that the column v[:,i] is the eigenvector 
# corresponding to the eigenvalue w[i].
# Calculate the decompositions of eigenvalue W and V right vectors.

W, Vr = eigh(A)
print("Eigen value W: ")
print(W)
print("Eigen Right Vector Vr: ")
print(Vr)

# define a square matrix 2x2
D = np.diag((-1,1))
print("A diagonal array D: ")
print(D)
W, Vr = eig(D)
print("Eigen value W: ")
print(W)
print("Eigen Right Vector Vr: ")
print(Vr)

# Reconstruct
B = np.diag(W.dot(Vr))
print("B = W*Vr: ")
print(B)

