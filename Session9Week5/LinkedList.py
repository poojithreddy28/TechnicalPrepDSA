class dog:
    def __init__(self,name,color):
        self.name = name 
        self.color = color
    def bark(self):
        print("{} is barking".format(self.name))
obj1 = dog("Ruby","Brown")
obj2 = dog("Max","Black")
print("My dog name is {} and its color is {}".format(obj1.name,obj1.color))
obj1.bark()
print("My dog name is {} and its color is {}".format(obj2.name,obj2.color))
obj2.bark()