from typing import Protocol

# 接口，其他类中只要明明为changeThing，即可以认为是一种Ichange的类
class IChange(Protocol):
    def changeThing(self, thing)->str:
        pass
