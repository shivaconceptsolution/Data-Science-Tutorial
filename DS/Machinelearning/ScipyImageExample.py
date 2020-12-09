from scipy import ndimage,misc
from matplotlib import pyplot as plt
import numpy as np
#get face image of panda from misc package
#panda =np.flipud(misc.face())
panda =misc.face()
panda1 = ndimage.rotate(panda, 135)
#plot or show image of face
plt.imshow( panda1 )
plt.show()
