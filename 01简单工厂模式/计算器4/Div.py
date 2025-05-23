from Operation import Operation

class Div(Operation):
    def getResult(self, numberA:int, numberB:int):
        if numberB == 0:
            print("除数不能为0！")
            raise ArithmeticError()
        return numberA / numberB