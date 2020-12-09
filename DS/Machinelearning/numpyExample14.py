import numpy as np
f = np.array([(1,2),(1,2)])
g = np.array([(1,4),(1,5)])
### 1*4+2*5
a=np.dot(f, g)
print(a)

b = np.matmul(f,g)
print(b)
