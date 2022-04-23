# method overriding

class Animal:
    def animal_voice(self):
        print("Animal roar")

    def animal_method(self):
        print("Animal class being called")


class Dog(Animal):
    def animal_voice(self):
        print("Dog Barks")

    def Dog_method(self):
        print("Dog class being called")

class Cat(Dog):
    def animal_voice(self):
        print("Cat Meuuuu")

    def cat_method(self):
        print("Cat class being called")


obj = Dog()

obj.animal_voice()
obj.animal_method()


