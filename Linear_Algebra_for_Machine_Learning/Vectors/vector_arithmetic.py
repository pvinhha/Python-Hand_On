from numpy import array
import random

# Create a reference list
numericList = [x for x in range(100)]
print("Reference list: ", numericList)
# Create a vector from a list
# A vector is a tuple of one or more values called scalars
v = array(numericList)
print("Vector v: ", v)

# Create 2 vectors with random values picked from the reference list
# Initialize as lists of 10 random numbers
a = []
b = []

for i in range(10):
    a.append(random.choice(numericList)) 
    b.append(random.choice(numericList))
    
# Make vectors from themselves
a = array(a)
b = array(b)
print("Vector a: ", a)
print("Vector b: ", b)

# Vector multiplication
c = a * b
print("\nVector multiplication resultant c=a*b : ", c)

# Vector division
print("Vector division resultant c=a/b : ", a/b)

# Vector addition
print("Vector addition resultant c=a+b : ", a+b)

# Vector substraction
print("Vector substraction resultant c=a-b : ", a-b)

# Vector dot product
# c = a.b = a[0]*b[0] + a[1]*b[1] + ...
c = 0
for i in range(len(a)):
    c += a[i]*b[i]

print("Vector dot product resultant c = a.b: ", c)

# Vector scalar multiplication
c = 2 * a
print("\nVector scalar multiplication resultant c=2*a : ", c)
