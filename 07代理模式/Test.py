
# 送礼物的接口
class IGiveGift:
    def give_dolls(self):
        pass

    def give_flowers(self):
        pass

    def give_chocolate(self):
        pass

class SchoolGirl:
    def get_name(self):
        return self.name

    def setName(self, value: str):
        self.name = value

# 追求者类
class Pursuit(IGiveGift):
    def __init__(self, mm: SchoolGirl):
        self.mm = mm

    def give_dolls(self):
        print(f"{self.mm.get_name()} 你好！送你洋娃娃")

    def give_flowers(self):
        print(f"{self.mm.get_name()} 你好！送你鲜花")

    def give_chocolate(self):
        print(f"{self.mm.get_name()} 你好！送你巧克力")

# 代理类
class Proxy(IGiveGift):
    # this.gg是追求者，mm是被追求者，代理需要两个都认识
    def __init__(self, mm: SchoolGirl):
        # 代理初始化的过程，实际是追求者初始化的过程
        self.gg = Pursuit(mm)

    # 代理在送礼物
    def give_dolls(self):
        # 实质上是追求者在送礼物
        self.gg.give_dolls()

    def give_flowers(self):
        self.gg.give_flowers()

    def give_chocolate(self):
        self.gg.give_chocolate()

if __name__ == "__main__":
    print("**********************************************")
    print("《大话设计模式》代码样例")
    girlLjj = SchoolGirl()
    girlLjj.setName("李娇娇")
    boyDl = Proxy(girlLjj)
    boyDl.give_dolls()
    boyDl.give_flowers()
    boyDl.give_chocolate()
    print("**********************************************")