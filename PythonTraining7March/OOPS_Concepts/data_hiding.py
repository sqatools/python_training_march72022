"""
_ single underscore
__ double under score
"""
class college:
    _college_name = 'IIT College'
    __course = 'data science'
    address = 'Mumbai'
    def __init__(self, college_fee, ranking, placement_per):
        self._college_fee = college_fee
        self.__ranking = ranking
        self.placement = placement_per
        self._show_ranking()

    def _show_ranking(self):
        print(f"collge ranking is : {self.__ranking}")


    def __show_placement_percentage(self):
        print(f"college placement percentage is : {self.placement}")

    def show_all_details(self):
        print(f"College name : {college._college_name}\n"
              f"College Course : {college.__course} \n"
              f"Addrees : {college.address}")



"""
-> any variable and method with are defined with single underscore '_' and double '__' wont show in
suggest list.

-> Variable name with '_' can be access directly with class object.
-> Variable/method with '__' can not access directly with have to use different way
   obj._<class name>__<variable name>

"""
if __name__ == '__main__':
    obj = college('1Lac', '10th', '90%')
    # print(obj.address)
    # print(obj._college_name)
    # print(obj._college__course)
    #
    # obj._show_ranking()
    # obj._college__show_placement_percentage()
    #
    # print(dir(obj))
    #





