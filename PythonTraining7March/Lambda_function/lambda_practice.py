# lambda arguments:expression

result = lambda x: x*10

print(result)
print(result(30))

result2 = lambda x, y, z : x+y+z
print(result2(20, 30, 40))

# Map : map function can provide multiple parameter a single function and get the output
def square(n):
    return n*n

list1 = [12, 5, 3, 7, 8, 2, 6]

map_output = list(map(square, list1))
print(map_output)

cube_output = list(map(lambda x:x**3, list1))
print(cube_output)

# filter

filter_output = list(filter(lambda x:x%2 != 0, list1))
print("filter output :", filter_output)

# reduce : reduce gives us a single output as per the expression , e.g addition of all the
tuple1 = (4, 3, 6, 2, 7)

from functools import reduce

reduce_output = reduce(lambda x, y: x+y, tuple1)
print("reduce_output: ", reduce_output)

tuple2 = ("Hello", "Good", "Morning", "Its", "AwesomeDay")

reduce_output2= reduce(lambda x, y: x+" "+y, tuple2)
print("reduce_output2:", reduce_output2)
