# _*_coding:utf-8_*_
class Cat:
    def __init__(self, name = "无名"):
        self.name = name
        self.shoutNum = 3

    def setShoutNum(self, value):
        self.shoutNum = value

    def getShoutNUm(self):
        return self.shoutNum

    def shout(self):
        result = ""
        for i in range(self.shoutNum):
            result += "喵"

        return f"我的名字叫：{self.name}, {result}"

if __name__ == "__main__":
    cat = Cat("小花")
    print(cat.shout())