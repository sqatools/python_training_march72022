import pandas as pd
import numpy as np
"""
info = {'Name' : ['John', 'Harry', 'Aaditya', 'Rahul'], 'ID' : [456, 346, 467, None],
        'salary' : ['50k', '40k', '30k', '20k']}

result = pd.DataFrame(info)

#print(result)
result['address'] = ['Pune', 'Mumbai', 'Delhi', 'Kolkata']

print(result)

print(result['Name'])

print(result['Name'][2])

print("_"*50)
##################################################################

names = ['John', 'Harry', 'Aaditya', 'Rahul', 'Mayank', 'Pradeep']
ID = [456, 346, 467]
salary = ['50k', '40k', '30k', '20k', '10k']

name_se = pd.Series(names, index= ['a', 'b', 'c', 'd', 'e', 'f'])
id_se = pd.Series(ID, index=['a', 'b', 'c'])
salary_se = pd.Series(salary, index=['a', 'b', 'c', 'd', 'e'])

info = {'Name' : name_se , 'ID' : id_se, 'salary' : salary_se}

result = pd.DataFrame(info)
print(result)
"""
#################################################################
"""
# Append method in data frame

#df_dict1 = {'name' : ('john', 'harry', 'rahul'), 'job' : ('QA', 'Dev', 'Admin')}
#df_dict1 = {'name' : 'john', 'job' : ('QA', 'Dev', 'Admin')}
#df_dict1 = ['john', 'harry', 'sejal']
df_dict1 = [['john', 'harry', 'sejal'], ['QA', 'Dev', 'Admin']]
df_dict2 = {'name' : ['john1', 'harry1', 'rahul1'], 'job' : ['HR', 'Sales', 'Marketing'], 'salary': ['40k', '50k', '60k']  }
df1 = pd.DataFrame(df_dict1)

#print(df1)

df2 = pd.DataFrame(df_dict2)

output = df1.append(df2, ignore_index=True)

print(output)

#print(output['salary'][2])
"""

##########################################################################
"""
# apply function to Dataframe

df1 = pd.DataFrame([[3, 5, 7], [5, 4, 2]], columns=['a', 'b', 'c'])

print(df1)

output = df1.apply(np.sqrt)
print(output)

sum_output = df1.apply(np.sum, axis=0)
print(sum_output)

sum_output2 = df1.apply(np.sum, axis=1)
print(sum_output2)
"""

##########################################################################
#Read csv file data using pandas

csv_data = pd.read_csv('user_data.csv')
#print(csv_data)

csv_data['Department'] = 'IT'

#print(csv_data)
#csv_data['Department'][2] = 'CS'
#print(csv_data['Department'][2])
#print(csv_data)

df1 = pd.DataFrame(csv_data)

#print(df1)

print(df1['Department'][2])

df1['Department'][2] = 'CS'

print(df1)









