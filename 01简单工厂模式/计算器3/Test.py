import Operation

if __name__ == "__main__":
    # 这里需要先创建对象，这样系统会默认传入self参数
    operate = Operation.Operation()
    a = int(input("请输入数字A："))
    b = int(input("请输入数字B："))
    op = input("请输入运算符：")
    result = operate.getResult(a, b, op)

    if result == None:
        print("计算任务失败")
    else:
        print(f"result = {result}")