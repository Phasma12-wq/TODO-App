from abc import ABC, abstractmethod
"""
    This section contains dataclasses from which the todo list and its items are created
"""
class todo(ABC):
    def __init__(self, name):
        self.name = name
        self._isDone = False

    @abstractmethod
    def markDone(self):
        pass

    @abstractmethod
    def getStr(self):
        pass

class todo_item(todo):
    def __init__(self, name):
        super().__init__(name)

    def markDone(self):
        self._isDone = True
    
    def getStr(self):
        status: str = "Done ✅" if self._isDone else "Pending"
        return f"{self.name} {status}"
