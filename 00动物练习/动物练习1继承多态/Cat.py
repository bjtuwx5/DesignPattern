import Animal

class Cat(Animal.Animal):
    def __init__(self, name):
        super().__init__(name)

    def shout(self):
        result = ""
        for i in range(self.shoutNum):
            result += "喵"

        return f"我的名字叫{self.name}{result}"