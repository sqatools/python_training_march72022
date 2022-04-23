from OOPS_Concepts.class_pqr import pqr
from OOPS_Concepts.class_def import efg

class xyz(pqr, efg):

    var_xyz = 'We are in class XYZ'
    def __init__(self, college_fee, ranking, placement_per):
        super().__init__(college_fee, ranking, placement_per)

    def show_class_xyz(self):
        print("This is class XYZ method")

    def operation(self):
        num1 = 40
        num2 = 6
        print("Square :", num1**num2)