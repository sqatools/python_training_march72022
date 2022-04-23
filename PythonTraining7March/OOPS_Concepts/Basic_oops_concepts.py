"""
class: class is nothing but a blue print of any object.
       e.g. before constructing the building, we have to create design of that building
       and that design or architecture of the building is known as class.

object: Object through which we can access the properties and attributes of the class.

constructor:
inheritance
polymorphism
data hiding
abstraction
"""

class student:

    def __init__(self, name):
        # instance variable
        self.name = name

    # instance method
    def show_name(self):
        print(f"My name is {self.name}")

# self : self is object of that class being created
#

obj = student('Sachine')
#obj.show_name()
student.show_name(obj)


# str1 = 'Hello'
# print(dir(obj))
# print(type(obj))
# print(type(str1))
# print(dir(str1))
#
