import numpy as np
dimensions=[5,15,25]
for n in dimensions:
    u = np.random.randint(25, size=(n))
    U=np.array([u])
    Unorm=np.linalg.norm(U, ord=2)
    v = np.random.randint(25, size=(n))
    V=np.array([v])
    Vnorm=np.linalg.norm(V, ord=2)
    U_transpose=U.T
    UVt=np.dot(U_transpose,V)
    UVtnorm=np.linalg.norm(UVt, ord=2)
    rank = np.linalg.matrix_rank(UVt)
    print('\n\n For N=',n, '\n The norm of U',Unorm, '\n The norm of V',Vnorm,'\n The norm of UVt',UVtnorm )
    print('\n\n The Rank of UVt is', rank)
    
    #print(V)

