import numpy as np
f = np.array([1,2,3])
g = np.array([4,5,6.0])

print('Horizontal Append:', np.hstack((f, g)))
print('Veritcal Append:', np.vstack((f, g)))
