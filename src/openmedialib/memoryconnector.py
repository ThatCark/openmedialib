from abc import ABC

class MemoryConnector(ABC):

    @abstractmethod
    def connect(self, db):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def loaf(self):
        pass
    
# C: Create
# R: Retrieve
# U: Update
# D: Delete