class Animal:
     def __init__(self):
        print("Animal constructor")

    # def speak(self):
    #     print("Animal makes sound")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog constructor")

d = Dog()
