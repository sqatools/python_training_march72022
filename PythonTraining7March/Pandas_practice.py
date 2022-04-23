# Series :
import pandas as pd
import numpy as np

"""


list1 = [5, 6, 3, 7, 23]

x = pd.Series(list1)

print(x)

new_arr = np.array(['P', 'a', 'n', 'd', 'a', 's'])
output = pd.Series(new_arr)

print(output)

info_data = {'name' : 'john', 'age': 30, 'address' : 'Mumbai', 'Mobile' : 4567}

output = pd.Series(info_data)
print(output)

list1 = [1, 3, 5, 7]

#output = pd.Series(4, index=list1)
#output = pd.Series([4, 5, 6, 78], index=list1)
output = pd.Series((4,5,  76, 6), index= [3, 2, 3, 4])

print(output)

output = pd.Series([1, 3, 5, 7, 8], index=['a', 'b', 'c', 'd', 'e'])
print(output.index)
print(output.shape)
print(output.dtype)
print(output.size)
print(output.empty)
print(output.values)
"""

a = pd.Series(['Java', 'C', 'C++', np.nan])
a.map({'Java':'Core'})

a.map('I like {}'.format, na_action='ignore')
print(a)







