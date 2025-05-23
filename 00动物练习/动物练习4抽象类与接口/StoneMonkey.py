import Monkey

class StoneMonkey(Monkey.Monkey):
    def __init__(self, name):
        super().__init__(name)

    # 重写父类Monkey的方法
    def getShoutSound(self):
        return "俺老孙来也！"

    # 接口实现
    def changeThing(self, thing):
        return f"{self.shout()}我会七十二变，可变出:{thing}"
