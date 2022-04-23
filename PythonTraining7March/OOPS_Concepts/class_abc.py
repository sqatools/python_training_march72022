from OOPS_Concepts.data_hiding import college

class abc(college):
    var_abc = 'We are in class ABC'

    def __init__(self, college_fee, ranking, placement_per):
        super().__init__(college_fee, ranking, placement_per)

    def show_class_abc(self):
        print("This is class ABC method")

    def operation(self):
        num1 = 40
        num2 = 60
        print("addition :", num1+num2)


    def show_all_college_details(self):
        print("college address :", self.address)
        print("college name :", self._college_name)
        print("college course", self._college__course)
