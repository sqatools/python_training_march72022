def function_test(*args):
    print(args)
    odd_list = []
    even_list = []
    for var in args:
        if var%2 == 0:
            odd_list.append(var)
        else:
            even_list.append(var)
    print(odd_list)
    print(even_list)

#function_test(3, 6, 2, 7, 6, 2, 24)

def function_dict_input(**kwargs):
    print(kwargs)
    db_username = 'john'
    db_password = 'P@ssw0rd'
    # verify login successful or not
    if kwargs['name'] == db_username and kwargs['password'] == db_password:
        print("login successful")
    else:
        print("invalid credentials")

#function_dict_input(password='P@ssw0rd', name='john', email='john@gmail.com')


def function_dict_input2(username, *args, **kwargs):
    print("name :", username)

    print(args)
    print(kwargs)
    db_username = 'john'
    db_password = 'admin@123'
    # verify login successful or not
    # for data in kwargs.items():
    #     print(data)
    temp_status = False
    for i in range(len(kwargs)+1):
        if kwargs['name'][i] == db_username and kwargs['password'][i] == db_password:
            print("login successful")
            temp_status = True
            break
        else:
            continue

    if not temp_status:
        print("invalid credentials")


#function_dict_input2('SQATools', 'pqr', 'xyz', name=['john', 'harry', 'Aditya'], password=['admin@123', 'pwd2', 'pwd3'])


# return statement in function.

"""
def addition_of_numbers(num1, num2):
    return num1+num2

def multiplication(num1, num2, num3):
    add_output = addition_of_numbers(num1, num2)
    result = add_output*num3
    return result

def divide(num1, num2):
    return num1//num2

output = addition_of_numbers(100, 200)
print(output)

output3 = multiplication(100, 300, 5)
print(output3)

print(divide(output3, 20))
"""

def sum_of_numbers(a, b, c, d):
    print(a+b+c+d)

def sum_of_numbers(a, b, c):
    print(a+b+c)

def sum_of_numbers(a, b):
    print(a+b)

#sum_of_numbers(40, 50, 60, 70)




