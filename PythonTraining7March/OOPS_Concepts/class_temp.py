from abc import ABC

class car(ABC):

    def car_milege(self):
        pass

    def car_has_total_tyre(self):
        print("This car has 4 wheels")


obj = car()
#obj.car_has_total_tyre()

str1 = 'Hello'
str1.replace()