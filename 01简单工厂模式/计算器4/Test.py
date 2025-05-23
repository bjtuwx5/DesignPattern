from OperationFactory import OperationFactory

if __name__ == "__main__":
    # 这里需要先创建对象，这样系统会默认传入self参数
    a = int(input("请输入数字A："))
    b = int(input("请输入数字B："))
    op = input("请输入运算符：")

    opr = OperationFactory.create_operate(op)
    if opr == None:
        print("计算任务失败")

    result = opr.getResult(a, b)

    print(f"result = {result}")