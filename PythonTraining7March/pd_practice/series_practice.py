import pandas as pd

index = [1, 4, 7]
list1 = ['Delhi', 'Mumbai', 'Agra']

data2 = {'a': 234, 'b' : 456, 'c': 334}

info = pd.Series(index= index, data= list1)
print(info)

info2 = pd.Series(data= data2)
print(info2)

info3 = pd.Series(['P', 'a', 'n', 'd', 'a', 's'])
print(info3)
print(info3[0])

info4 = pd.Series(data=4, index=[1, 3, 5, 6, 7])
print(info4[1])
