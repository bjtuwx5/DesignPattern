from abc import ABC, abstractmethod
class Operation(ABC):
    @abstractmethod
    def getResult(self, numberA:int, numberB:int):
        return 0