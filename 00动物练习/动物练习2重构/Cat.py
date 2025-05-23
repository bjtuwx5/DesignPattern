import Animal

class Cat(Animal.Animal):
    def __init__(self, name):
        super().__init__(name)

    def getShoutSound(self):
        return "喵"