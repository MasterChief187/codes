# codes
IME work python
import numpy as np
P1=np.array([(-0.40825,0.43644,0.80178),(-0.8165,0.21822,-0.53452),(-0.40825,-0.87287,0.26726)])
P2=np.array([(-0.51450,0.48507,0.70711),(-0.68599,-0.72761,0.0000),(0.51450,-0.48507,0.70711)])
P3=np.array([(-0.58835,0.70206,0.40119),(-0.78446,-0.37524,-0.49377),(-0.19612,-0.60523,0.77152)])
P4=np.array([(-0.47624,-0.4264,0.30151),(0.087932,0.86603,-0.40825),(-0.87491,-0.26112,0.86164)])

def is_orthogonal_by_definition(sqrd_matrix):
    error=0
    while error==0:
        rows,columns=sqrd_matrix.shape
        if rows!=columns:
            print('\n This not a Square Matrix.\n')
            error=error+1
        elif rows<=0 or columns<=0:
            print('\n This not a Square Matrix.\n')
            error=error+1
        sqrd_matrix_T=np.transpose(sqrd_matrix)
        MMT=np.dot(sqrd_matrix,sqrd_matrix_T)
        Identity=np.array(np.eye(rows,dtype=float))
        print('\n Matrix is orthogonal by definition: ',np.allclose(MMT,Identity,rtol=1e-3, atol=1e-05))
        error=1
        
is_orthogonal_by_definition(P1)
is_orthogonal_by_definition(P2)
is_orthogonal_by_definition(P3)
is_orthogonal_by_definition(P4)

def is_orthogonal_by_vector(sqrd_matrix):
    error=0
    count=0
    while error==0:
        rows,columns=sqrd_matrix.shape
        if rows!=columns:
            print('\n This not a Square Matrix.\n')
            error=error+1
        elif rows<=0 or columns<=0:
            print('\n This not a Square Matrix.\n')
            error=error+1
        for i in range(rows):
            column  = sqrd_matrix[:, i]
            norm=np.linalg.norm(column)
            print(norm)
            answer=np.isclose(norm,1)

            if answer==True:
                count=count+1
        if count==rows:
           print('\n Matrix is orthogonal by vector: ',answer)
        else:
            print('\n Matrix is orthogonal by is orthoganol by vector: false')
            
        error=1

is_orthogonal_by_vector(P1)
is_orthogonal_by_vector(P2)
is_orthogonal_by_vector(P3)
is_orthogonal_by_vector(P4)
