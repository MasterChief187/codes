import numpy as np

def alc_cholesky(A):
    n = len(A)
    R = np.zeros((n,n))
    for i in range(n):
        Summation1 = 0
        for j in range(i):
            Summation1 += R[j,i]*R[j,i]
        tmp = A[i,i] - Summation1
        if tmp <= 0:
            raise Exception("THE ENTRY IS NOT DEFINITELY POSITIVE")
        R[i,i] = tmp**(0.5)
        for j in range(i+1,n):
            Summation2 = 0
            for k in range(i):
                Summation2 += R[k,i]*R[k,j]
            R[i,j] = (A[i,j] - Summation2)/R[i,i]
    return R

# Check
A = np.array([[1 , 1, 4,-1],
                [1 , 5, 0,-1],
                [4 , 0,21,-4],
                [-1,-1,-4,10]])
R = alc_cholesky(A)
print("A=R^T @ R ?", np.allclose(R.T @ R, A))

