class Animal:
    def __init__(self, name = "无名"):
        self.name = name
        self.shoutNum = 3

    def setShoutNum(self, value):
        self.shoutNum = value

    def getShoutNUm(self):
        return self.shoutNum

    def shout(self):
        return ""