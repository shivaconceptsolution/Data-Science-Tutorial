import pandas as pd
import numpy as np

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel.from_dict(data,orient ='minor')
print(p)
