from abc import *
class computer(ABC):
    @abstractmethod
    def name(self):
        pass

o=computer()
o.name()