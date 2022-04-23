"""
MRO : Method Resolution Order
"""

class sci_stu:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


    def show_student_data(self):
        print(f"Name : {self.name}\n"
              f"Age : {self.age}\n"
              f"email : {self.email}")

class math_stu:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_student_data(self):
        print(f"Name : {self.name}\n"
              f"Age : {self.age}\n")

"""
MRO : (Method Resolution Order) :  
when we call two class together and have same method name, then first
calling class method will get first preference.
"""
class college(math_stu, sci_stu):
     def __init__(self, name, age, email):
         super().__init__(name, age)

     def print_msg(self):
         print("We are in college class")

     # def show_student_data(self):
     #     print("this method belongs to college class")


obj = college('Rohit', '20', 'rahit@gmail.com')

obj.show_student_data()
