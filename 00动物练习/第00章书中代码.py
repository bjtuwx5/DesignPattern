# _*_coding:utf-8_*_

class Animal:
    def __init__(self, name="无名"):
        self.name = name
        self.shoutNum = 3

    def setShoutNum(self, value):
        self.shoutNum = value

    def getShoutNUm(self):
        return self.shoutNum

    def getShoutSound(self):
        return ""

    def shout(self):
        result = ""
        for i in range(self.shoutNum):
            result += self.getShoutSound()+", "
        return f"我的名字叫{self.name}{result}"

class Cat(Animal):
    def getShoutSound(self):
        return "喵"

class Dog(Animal):
    def getShoutSound(self):
        return "汪"

class Cattle(Animal):
    def getShoutSound(self):
        return "哞"

class Sheep(Animal):
    def getShoutSound(self):
        return "咩"

if __name__ == "__main__":
    arrayAnimal = {
        Cat("小花"),
        Dog("阿毛"),
        Dog("小黑"),
        Cat("娇娇"),
        Cat("咪咪")
    }

    for animal in arrayAnimal:
        print(animal.shout())