from abc import ABC, abstractmethod

class MemoryConnector(ABC):

    @abstractmethod
    def connect(self, db):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def save(self, *data):
        pass

    @abstractmethod
    def load(self):
        pass
    
# C: Create
# R: Retrieve
# U: Update
# D: Delete