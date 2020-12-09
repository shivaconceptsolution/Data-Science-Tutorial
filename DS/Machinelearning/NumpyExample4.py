import numpy as np
size = int(input("enter size of array"))

a  = np.array([int]*size,ndmin=1)
for i in range(0,size):
    a[i]=int(input("enter element for "+str(i)+" index"))
print(a)
