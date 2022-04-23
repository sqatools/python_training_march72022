# def addition(a, b):
#     print(a+b)

def outer_function(func):
    def inner(x, y):
        print("output of given function:")
        return func(x, y)
    return inner


#addition_output = outer_function(addition)

#addition_output(30, 40)

@outer_function
def addition(a, b):
    return a+b

result = addition(50, 60)
print(result)

# @outer_function
# def multiplication(x, y):
#     print(x*y)


#multiplication(20, 3)

# program : write a python program to get all prime numbers from 1 to 100 using decorator.
# program : write a python program to list of factorial of all prime number from 1 to 20
#           using decorator