import numpy as np
A = np.matrix(np.ones((4,4)))
print(A)
np.asarray(A)[2]=5
print(A)
