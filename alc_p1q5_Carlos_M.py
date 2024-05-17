import numpy as np

def inversa_eliminacao(nxn_matrix):
    nxn_matrix= np.array(nxn_matrix)
    rows,columns=nxn_matrix.shape
    if rows!=columns:
        print('This is not a squared matrix')
        return error_in_dimensions
    
    Identity=np.eye(rows)
    Augmented=np.zeros(rows,2*rows)
    for m in range(rows):
        for n in range(rows):
            Augmented[m,n]=nxn_matrix[m,n]
            Augmented[m,n]=Identity[m,n]
            
    for n in range(rows):
        if Augmented[n,n]==0 and n!=0:
            print('try another method to find inverse')
    for n in range(rows):
         Augmented[n]=Augmented(n)/Augmented[n,n]
    for m in range(rows):
        n=0
        if (n+1)<rows and m<(rows-n):
            Augmented[rows-n]=(Augmented(rows-n,m)*Augmented[rows-(n+1)])-Augmented[rows-n]
            n=n+1
    for m in range(rows):
        n=0
        if (n+1)<rows and m!=n:
            Augmented[rows-n]=(Augmented(rows-n,rows-m)*Augmented[rows-(n+1)])-Augmented[rows-n]
            n=n+1
    for n in range(rows):
        if Augmented[n,n]==0 and n!=0:
            print('try another method to find inverse')
    for n in range(rows):
         Augmented[n]=Augmented(n)/Augmented[n,n]

    Ainverse=Augmented[:,n:]
    print(Ainverse)
    return Ainverse