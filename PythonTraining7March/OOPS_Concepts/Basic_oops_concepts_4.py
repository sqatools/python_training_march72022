class car:
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
        # print(cls.model) # can't instance variable with cls

    @staticmethod
    def first_static_method(fact_num):
        fact = 1
        for i in range(1, fact_num + 1):
            fact = fact * i

        return fact

if __name__ == '__main__':
    obj = car('Swift', '2020', '7Lac')
    print(obj.model)

    #obj.set_model_name('Celerio')
    #print(obj.model)

    obj.__setattr__('model', 'Dezire')
    print(obj.model)

    print(obj.__getattribute__('model'))

    obj.shows_car_information()