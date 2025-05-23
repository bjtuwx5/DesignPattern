from Add import Add
from Sub import Sub
from Div import Div
from Mul import Mul

class OperationFactory:
    @staticmethod
    def create_operate(operate):
        opr = None
        if operate == "+":
            opr = Add()
        elif operate == "-":
            opr = Sub()
        elif operate == "*":
            opr = Mul()
        elif operate == "/":
            opr = Div()
        else:
            print("输入非法")
            return None
        return opr
