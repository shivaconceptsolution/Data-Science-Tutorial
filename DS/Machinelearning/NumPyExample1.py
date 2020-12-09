import numpy as np 
a = np.array([[1, 2], [3, 4]])
#a = np.array([1, 2, 3,4,5], ndmin = 2)
print(a[0][0])
print(a)
for arr in a:
    for a1 in arr:
        print(a1,end='')
    print()    
         


