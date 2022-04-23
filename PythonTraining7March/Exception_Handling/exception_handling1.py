from Modules.modul_file3 import *

"""
try:
    code
except:
     message
"""

var1 = 100
var2 = 'Hello'

def add_two_variables(var1, var2):
    try:
        output = var1 + var2
        print(output)
    except Exception as e:
        #raise e
        print("Can not add string and integer, please provide same data for both variables")


#add_two_variables(var1, 200)

# Exception with else condition

def multiply_variables(var1, var2, filename):
    try:
        output = var1 * var2
        print(output)

        # read entire file
        with open(filename, 'r') as file:
            data = file.read()
            print(data)

    except Exception as e:
        print("Can not multiply not integer data")
        #raise e

    else:
        print("Multiplication Successful")
        for i in range(1, 11):
            print(i,"*",var1 ,"=", i*var1)


#file_path = 'E:\\Trainings\\PythonTraining7March\\file_input_ouput\\read_file.txt'

#multiply_variables(100, 300, file_path)

def multiply(num1, num2):
    try:
        output = num1*num2
        print(output)
    except Exception as e:
        print("can not multiple non integer data")
        #raise e

def read_entire_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            print(data)
    except Exception as e:
        print("File is not available")
        raise e

def multiply_variables2(var1, var2, filename):
    try:
        multiply(var1, var2)
        read_entire_file(filename)
    except Exception as e:
        print("multiplication operation failed")
        raise e

    else:
        print("Multiplication Successful")
        for i in range(1, 11):
            print(i,"*",var1 ,"=", i*var1)

# file_path = 'E:\\Trainings\\PythonTraining7March\\file_input_ouput\\read_file.txt'
# num1= '5'
# num2 = '10'
# multiply_variables2(num1, num2, file_path)


def exception_with_finally_Statement(num1, num2, filename):
    try:
       output = num1*num2
       print(output)
    except Exception as e:
        print("can not multiple non integer data")
    else:
        print("Congratulation there is no exception in the code")
    finally:
        read_entire_file(filename)
        print(addition(40, 50))


file_path = 'E:\\Trainings\\PythonTraining7March\\file_input_ouput\\read_file.txt'
num1= '10'
num2 = '15'
exception_with_finally_Statement(num1, num2, file_path)