import Cat

class MachineCat(Cat.Cat):
    def __init__(self, name):
        super().__init__(name)

    # 接口实现
    def changeThing(self, thing):
        return f"{super().shout()}我有万能的口袋，可以变出:{thing}"
