class Animal:
    ani_type="Lion"

    def __init__ (self ,animal_type , animal_sound):
        self.animal_type=animal_type
        self.animal_sound=animal_sound

    def show(self):
        print("Animal Type :",self.animal_type)
        print("Animal Sound:",self.animal_sound)

    @classmethod
    def get_type(cls):
        return cls.ani_type

    @classmethod
    def set_type(cls,ani_type):
        cls.ani_type=ani_type

    @staticmethod
    def sound(x):
        return x


a1=Animal("Dog","Bark")
a1.show()

print(Animal.get_type())

Animal.set_type("Dog")
print(Animal.get_type())

print(Animal.sound("Meow"))
    
