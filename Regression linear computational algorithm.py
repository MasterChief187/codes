import numpy as np


a=1
while a == 1:
    error=0
    m = int(input('\nHow many rows are in your matrix: '))  # Number of rows
    n = m                                                   # Number of rows # Number of columns
    if m==0:
       m=m+1
       
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    print('\n \n Enter triangular matrix')
    print('\n Enter elements beginning at row 1 column 1.')
    print("\n followed all elements of that row before moving to the others .")
    
    b = 0
    while b < n:
        c=0
        while c < m :
            matrix[b][c] = int(input('\n please enter square matrix: '))
            c = c + 1
            print(matrix)

        b=b + 1
    
    b=m-1
    e=1
    Msum=0
# Check for triangular matrix
    while b != 0:
        c=0
        while c < m-e :
            Msum= Msum + matrix[b][c] 
            c = c + 1
        e=e + 1
        b=b-1
         
    if Msum != 0:
        print('Error1 \n This is not a triangular matrix')
        error=error+1
    b=m-1
    e=0
    while b>0 : 
        if  matrix [b] [b]==0:
            print('\n Error2 \n Null in leading diaganol  Matrix')
            error=error+1
            b=0
        else:
            b=b-1
    
    if error==0:
        a=a+1

if error==0:
    print('\nGood matrix')

vector = [0 for _ in range(n)]
c=0
while c < m :
    vector [c] = int(input('\n please enter vector: '))
    c = c + 1
    print(vector)

e=1
f=0
a=m-1
b=a
vX = [0 for _ in range(n)]

vX[a] = vector[a]/matrix[a][b]
print('\n',vX)

while a>0:
    sum=0
    while a!=b:
      sum=sum+(matrix[a-1][b]*vX[b])
      b=b-1

    vX[a-1]=(vector[a-1]-sum)/matrix[a-1][b-1]
    a=a-1
print('\n YOUR RESULTING VECTOR IS X = ',np.transpose(vX))