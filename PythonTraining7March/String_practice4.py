"""
Create a python project for fruit shop
1. Should show fruit menu with price
2. User should able to select fruit and quantity.
3. User should able to select multiple fruits
3. Generate a bill as per user selection.

Solution Steps :
step1 : Create a list of fruits and their prices
        fruit_list = [['mango', 20], ['apple', 30], ['banana', 10]]
step2 :
        apply a loop and show the menu with select option.
"""

"""
while True:
    # Show fruits menu
    fruit_list = [['mango', 20], ['apple', 30], ['banana', 10], ['lichi', 40], ['pinnaple', 80]]

    print("Please select your fruit and enter quantity from menu:")

    for i in range(len(fruit_list)):
        print(f"{i}, {fruit_list[i][0]}, {fruit_list[i][1]}")

    # Get user input for fruits and price
    input_list = []
    while True:
        fruit = int(input("Please select fruit from list: e.g 0 or 1 or 2 :"))
        qua = int(input("Please enter your quantity : "))
        input_list.append((fruit, qua))
        more = input("do you want to select more fruit.. yes/no :")
        print("--"*10)
        if more == 'yes':
            continue
        else:
            break
    result_list = []
    for data in input_list:
        if data[0] <= len(fruit_list):
            selected_number = data[0]
            fruit_name = fruit_list[data[0]][0]
            fruit_prince = fruit_list[data[0]][1]
            fruit_quantity = data[1]
            fruit_bill = fruit_prince*fruit_quantity
            result_list.append((selected_number, fruit_name, fruit_prince, fruit_quantity, fruit_bill))
            # Generate bill
        else:
            result_list.append((data[0], 'No', 0, 0, 0))
    print(result_list)

    # Generate total bill
    total_bill = 0
    print("------------Customer Bill-----------")
    print("Selection,  Fruit Name, Price, Quantity, Amount ")
    for fruit_data in result_list:
        print(fruit_data[0], ":", fruit_data[1], ":", fruit_data[2], ":", fruit_data[3], ":", fruit_data[4])
        total_bill = total_bill + fruit_data[4]
    print("-------------------------------------")
    print("Total Bill :", total_bill)
    print("####"*10)
    print("\n")

"""

dict2 = {'b': 4, 'c': 'Hello', 'd': [4, 5, 6], 'e': [7, 8, 9]}

key_data = dict2.keys()
value_data = dict2.values()

print(key_data)
print(value_data)

for key in key_data:
    print(key)
print("*"*20)
for val in value_data:
    print(val)


list1 = list(key_data)
value_list = list(value_data)

print(list1)

print(list1[0])
print(value_list)


