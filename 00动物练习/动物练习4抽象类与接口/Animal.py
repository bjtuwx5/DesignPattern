import abc
class Animal(abc.ABC):
    def __init__(self, name = "无名"):
        self.name = name
        self.shoutNum = 3

    def setShoutNum(self, value):
        self.shoutNum = value

    def getShoutNUm(self):
        return self.shoutNum

    # 抽象类方法声明，子类必须实现
    @abc.abstractmethod
    def getShoutSound(self)->str:
        pass

    def shout(self):
        result = ""
        for i in range(self.shoutNum):
            result += self.getShoutSound() + ","
        return f"我的名字叫：{self.name}, {result}"