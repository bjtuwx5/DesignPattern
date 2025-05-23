class Animal:
    def __init__(self, name = "无名"):
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
            result += self.getShoutSound() + ","
        return f"我的名字叫：{self.name}, {result}"