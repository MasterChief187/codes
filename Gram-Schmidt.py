import numpy as np

def modified_gram_schmidt(A):
   
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    
    for j in range(n):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]
    
    return Q, R

# Testing the implementation with Exercise 14.15

# Example matrix for testing
A = np.array([
    [12, -51, 4],
    [6, 167, -68],
    [-4, 24, -41]
])

# Using the modified Gram-Schmidt function
Q, R = modified_gram_schmidt(A)

print("Q matrix from modified Gram-Schmidt:")
print(Q)
print("\nR matrix from modified Gram-Schmidt:")
print(R)

# Comparing with numpy.linalg.qr
Q_np, R_np = np.linalg.qr(A)

print("\nQ matrix from numpy.linalg.qr:")
print(Q_np)
print("\nR matrix from numpy.linalg.qr:")
print(R_np)
