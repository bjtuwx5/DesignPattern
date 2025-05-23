import math
class CashSuper:
    def acceptCash(self, price, num):
        pass

class CashNormal(CashSuper):
    def acceptCash(self, price, num):
        return price * num

class CashRebate(CashSuper):
    def __init__(self, moneyRebate):
        self.moneyRebate = moneyRebate

    def acceptCash(self, price, num):
        return price * num * self.moneyRebate

class CashReturn(CashSuper):
    def __init__(self, moneyCondition, moneyReturn):
        # 返利条件
        self.moneyCondition = moneyCondition
        # 返利值，比如“满300返100”，就是moneyCondition=300,moneyReturn=100
        self.moneyReturn = moneyReturn

    def acceptCash(self, price, num):
        result = price * num
        if self.moneyCondition > 0 and result >= self.moneyCondition:
            result = result - math.floor(result / self.moneyCondition) * self.moneyReturn
        return result

class CashContext:
    def __init__(self, cashType):
        if cashType == 1:
            self.cs = CashNormal()
        elif cashType == 2:
            self.cs = CashRebate(0.8)
        elif cashType == 3:
            self.cs = CashRebate(0.7)
        elif cashType == 4:
            self.cs = CashReturn(300, 100)
        else:
            pass
    def getResult(self, price, num):
        return self.cs.acceptCash(price, num)

if __name__ == "__main__":
    # 商品折扣模式(1.正常收费 2.打八折 3.打七折)
    discount = int(input("请输入商品折扣模式（1.正常收费 2.打八折 3.打七折 4.满300送100）："))
    price = int(input("请输入商品单价："))
    num = int(input("请输入商品数量："))

    if price <= 0 or num <= 0:
        print("输入不能为0！")

    # 根据用户输入，将对应的策略对象作为参数传入CashContext对象中
    cc = CashContext(discount)
    # 通过Context的getResult方法的调用，可以得到收取费用的结果
    # 让具体算法与客户进行了隔离
    # 当前商品合计费用
    totalPrices = cc.getResult(price, num)
    print(f"单价：{price}元 数量：{num} 合计：{totalPrices}元")



