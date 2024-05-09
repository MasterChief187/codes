import numpy as np
import math 

angle1=float(input('\nPlease enter angle #1 :' ))
angle2=float(input('\nPlease enter angle #2\n :' ))

L1=np.matrix([[20*math.cos((angle1/180)*math.pi)],[20*math.sin((angle1/180)*math.pi)],[-1]])
L2=np.matrix([[15*math.cos((angle1/180)*math.pi)],[15*math.sin((angle1/180)*math.pi)],[1]])

L1minus=(-1)*L1

Translation=[[1,0,0],[0,1,0],[0,0,1]]
Translation2=[[1,0,0],[0,1,0],[0,0,1]]
Translation[0][2]=int(L1minus[0][0])
Translation[1][2]=int(L1minus[1][0])
Translation2[0][2]=float(L1[0][0])
Translation2[1][2]=float(L1[1][0])
L2T=np.dot(Translation,L2)
print('\n\n the final positiontranslation ', L2T)

print('\n\n the final posiL###3on \n', L1)
print('\n\n the final posiranslation2 is \n', L2)
print('\n\n the final positiontranslation \n', Translation)
rotation=np.array([[math.cos((angle2/180)*math.pi),-math.sin((angle2/180)*math.pi),0],[math.sin((angle2/180)*math.pi),math.cos((angle2/180)*math.pi),0],[0,0,1]])
L2o=np.dot(rotation,L2T)
L2RT=np.dot(Translation2,L2o)
print('\n\n the final position L3minus is \n',L2o)
print('\n\n the final position of the arm is ', L2RT)