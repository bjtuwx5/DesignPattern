import Animal

class Dog(Animal.Animal):
    def __init__(self, name):
        super().__init__(name)

    def shout(self):
        result = ""
        for i in range(self.shoutNum):
            result += "汪"

        return f"我的名字叫{self.name}{result}"