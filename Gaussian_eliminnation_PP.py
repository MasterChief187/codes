import numpy as np
from scipy.linalg import lu

def gaussian_elimination_partial_pivoting(A, b):
    n = len(b)
    # Create an augmented matrix
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    for i in range(n):
        # Partial pivoting
        max_row = np.argmax(np.abs(Ab[i:n, i])) + i
        if i != max_row:
            Ab[[i, max_row]] = Ab[[max_row, i]]
        
        # Elimination process
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])) / Ab[i, i]
    
    return x

# Example usage
A = np.array([[3, 2, -4],
              [2, 3, 3],
              [5, -3, 1]], dtype=float)
b = np.array([3, 15, 14], dtype=float)

x_gaussian = gaussian_elimination_partial_pivoting(A, b)
print("Solution from Gaussian Elimination with Partial Pivoting:", x_gaussian)

# Compare with scipy.linalg.lu
P, L, U = lu(A)

# Compute the solution using the LU decomposition from SciPy
def lu_solve(L, U, P, b):
    # Solve Ly = Pb
    Pb = np.dot(P, b)
    y = np.zeros_like(b)
    for i in range(len(y)):
        y[i] = Pb[i] - np.dot(L[i, :i], y[:i])
    
    # Solve Ux = y
    x = np.zeros_like(y)
    for i in range(len(x) - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
    
    return x

x_scipy = lu_solve(L, U, P, b)
print("Solution from SciPy LU Decomposition:", x_scipy)