import numpy as np
from scipy import io as sio
arr = np.ones((4,4))
sio.savemat('example.mat',{'ar':arr})
data = sio.loadmat('example.mat', struct_as_record=True)
print(data['ar'])

