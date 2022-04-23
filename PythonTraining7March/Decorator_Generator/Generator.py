"""
def show_number():
    for i in range(1, 10):
        if i%3 == 0:
            yield i


output = show_number()
print(output)

for data in output:
    print(data)


# def function_with_return():
#     str1 = "Hello Goode Mornnig"
#     return str1
#
#    str2 = "Its Python Programming"
#    return str2

def function_with_yield():
    str1 = "Hello Good Morning"
    yield str1

    str2 = "Python Programming"
    yield str2

    str3 = "We are learning"
    yield str3

result = function_with_yield()
#print(result)
print(next(result))
print(next(result))
print(next(result))
#print(next(result))

list1 = [5, 4, 3, 8, 2]

result = [x**2 for x in list1]
print(result)

#Generator expression
result2 = (x**2 for x in list1)
print(result2)
#
# for i in result2:
#     print(i)

print(next(result2))
print(next(result2))
"""

#####################################
import sys

# list expression with 1 million
list_result = [i**2 for i in range(10000)]

print("Memory by list express:", sys.getsizeof(list_result))

generate_result = (j**2 for j in range(10000))

print("Memory by Generator :", sys.getsizeof(generate_result))

