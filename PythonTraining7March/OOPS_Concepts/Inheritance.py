"""
Inheritance : aqure the property one class by another class is known as inheritance.

-> single inheritance : Class A -> Class B
-> multi level inheritance : Class A -> Class B -> Class C
-> multiple inheritance : Class A -> Class B, CLass C -> Class B

"""
"""
# parent class
class abc:
    def show_msg(self):
        print("we are in class abc")

# child class
class xyz(abc):
    def show_xyz_msg(self):
        print("we are in class xyz")


obj = xyz()

obj.show_xyz_msg()
obj.show_msg()
"""

"""
# parent class
class school:
    def __init__(self, sch_name,  result):
        self.sch_name = sch_name
        self.result = result

    def show_school_name(self):
        print(f"Students are learning in : {self.sch_name}")

    def show_result(self):
        print(f"The student exam result is : {self.result}")

# child class
class student(school):
    def __init__(self, sch_name, result, stu_name, stu_rollno):
        super().__init__(sch_name, result)
        self.name = stu_name
        self.rollno = stu_rollno

    def show_student_details(self):
        print(f"School name: {self.sch_name}\n"
              f"Student name : {self.name}\n"
              f"Student roll No : {self.rollno}")



st_obj = student('Higher Sec School', 'Pass', 'Rohit', '454')

st_obj.show_student_details()
st_obj.show_result()

#

"""
"""
# Multilevel inheritance

class A:
    var_a = 'We are in class A'

    def show_class_A(self):
        print("This is class A method")


class B(A):
    var_b = 'We are in class B'

    def show_class_B(self):
        print("This is class B method")


class C(B):
    var_c = 'We are in class C'

    def show_class_C(self):
        print("This is class C method")

class D(C):
    var_c = 'We are in class D'

    def show_class_D(self):
        print("This is class D method")

if __name__ == '__main__':
    obja = A()
    obja.show_class_A()

    print("_"*50)
    objb = B()
    objb.show_class_A()
    objb.show_class_B()
    print("_"*50)
    objc = C()
    objc.show_class_C()
    objc.show_class_A()
    objc.show_class_B()

"""


##################################################
# multiple inheritance

# A -> C
# B -> C

class A:
    var_a = 'We are in class A'

    def show_class_A(self):
        print("This is class A method")


class B:
    var_b = 'We are in class B'

    def show_class_B(self):
        print("This is class B method")


class C(A, B):
    var_c = 'We are in class C'

    def show_class_C(self):
        print("This is class C method")


if __name__ == '__main__':
    objc = C()
    print(objc.var_b)


