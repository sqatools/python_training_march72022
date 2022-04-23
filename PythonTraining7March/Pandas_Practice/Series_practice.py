import pandas as pd

"""
list1 = [3, 2, 5, 7]

output = pd.Series(list1)
print(output)

print(output[0])

print("_"*20)
# user defined index for the data

output2 = pd.Series(list1, index=['a', 'b', 'c', 'd'])
print(output2)

print(output2['a'])
print(output2[2])

print("_"*20)
output3 = pd.Series(4, index=[1, 2, 3, 4, 5, 6])
print(output3)

print("_"*20)
# Series with Dictionary

dict1 = {'name' : 'Rohit', 'job Title': 'Developer', 'Salary' : '50k' , 'email': 'rohit@test.com'}

dict_output = pd.Series(dict1)
print(dict_output)

print("_"*20)
str_list = ['P', 'y', 't', 'h', 'o', 'n']
output4  =pd.Series(str_list)

print(output4)

print("index:", output4.index)
print("shape:", output4.shape)
print("size:", output4.size)
print("_"*30)
#######################################################
#Create data frame with series

fruits = ['Apple', 'Banana', 'Mango', 'Cherry']
price = [50, 40, 800, 500]
quantity = [30, 40, 10, 20]
fruits_bill = []
for i in range(len(price)):
    fruits_bill.append(price[i]*quantity[i])
print(fruits_bill)

fruits_series = pd.Series(fruits)
price_series = pd.Series(price)
quantity_series = pd.Series(quantity)
bill_series = pd.Series(fruits_bill)

frame = {'Fruits' : fruits_series, 'Price': price_series, 'Quantity' : quantity_series, 'Bill' : bill_series}
#
output = pd.DataFrame(frame)
print(output)
"""

######################################
#Get Count of data in the list

list11 = [3, 6, 8, 3, 1, 2, 1, 2, 6]

output = pd.Index(list11)

print(output.value_counts())





