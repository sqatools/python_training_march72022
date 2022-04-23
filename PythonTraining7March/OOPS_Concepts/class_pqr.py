from OOPS_Concepts.class_abc import abc

class pqr(abc):
    var_pqr = 'We are in class PQR'

    def __init__(self, college_fee, ranking, placement_per):
        super().__init__(college_fee, ranking, placement_per)

    def show_class_pqr(self):
        print("This is class PQR method")

    def operation(self):
        num1 = 40
        num2 = 60
        print("Division :", num1//num2)