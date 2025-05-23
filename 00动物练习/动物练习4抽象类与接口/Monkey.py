import Animal

class Monkey(Animal.Animal):
    def __init__(self, name):
        super().__init__(name)

    # 抽象类方法的实现
    def getShoutSound(self):
        return "吱"