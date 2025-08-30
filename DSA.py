
# How to make classes and work in python 


class Human:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    def __str__(self):
        return "Hi my name is " + self.name + " and I am " + str(self.age) + " years old."
    def __checkage__(self,age):
        if(self.age > age):
            print("Our age is bigger")
        else:
            print("Thier age is bigger")

a = "arnav"
b = "20"
t = Human(a, b)
# print(t)

t.__checkage__(20)

'''hello '''