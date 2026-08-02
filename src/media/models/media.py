from abc import ABC, abstractmethod

class Media(ABC):
    
    @property
    @abstractmethod
    def owner(self):
        pass

    @property
    @abstractmethod
    def creator(self):
        pass

    @property
    @abstractmethod
    def release(self):
        pass