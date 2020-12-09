from scipy import linalg
import numpy as np
two_d_array = np.array([[4,5],[3,2]])
print(linalg.det( two_d_array ))
print(linalg.inv( two_d_array ))
eg_val, eg_vect = linalg.eig(two_d_array)
#get eigenvalues
print(eg_val)
#get eigenvectors
print(eg_vect)
