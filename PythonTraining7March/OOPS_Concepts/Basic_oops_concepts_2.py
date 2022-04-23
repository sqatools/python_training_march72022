class car:
    """
    This class is created to get all information about
    car models.
    """
    #class variable
    company = 'Suzuki'

    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def shows_car_information(self):
        print(f"name : {self.model}\n"
              f"year : {self.year}\n"
              f"price : {self.price}")

    def set_model_name(self, model):
        self.model = model

    @classmethod
    def first_class_method(cls):
        print(cls.company)
        #print(cls.model) # can't instance variable with cls

    @staticmethod
    def first_static_method(fact_num):
        fact =1
        for i in range(1, fact_num+1):
            fact = fact*i

        return fact



if __name__ == '__main__':

    obj = car('Celerio', 2022, '5lac')
    obj.shows_car_information()

    obj.set_model_name('Swift')
    obj.shows_car_information()

    print(obj.__module__)
    print(car.company)
    print(obj.company)
    obj.first_class_method()
    print(obj.first_static_method(7))
