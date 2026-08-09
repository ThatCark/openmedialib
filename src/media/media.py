from abc import ABC, abstractmethod

class Media(ABC):
    
    @property
    @abstractmethod
    def creator(self):
        pass

    @property
    @abstractmethod
    def release(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass
