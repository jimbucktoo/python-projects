import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

result1 = pd.Series(my_data,labels)
print(result1)

result2 = pd.Series(d)
print(result2)
