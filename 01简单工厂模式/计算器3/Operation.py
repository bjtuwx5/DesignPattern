class Operation:
    def getResult(self, a:int, b:int, operate:str)->int:
        result = 0
        if operate == '+':
            result = a + b
        elif operate == '-':
            result = a - b
        elif operate == '*':
            result = a * b
        elif operate == '/':
            if b == 0:
                print("输入数据非法")
                return None
            result = a / b
        elif operate == 'pow':
            result = pow(a, b)
        else:
            print("输入运算符非法类型")
            return None
        return result
