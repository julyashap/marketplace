from abc import ABC, abstractmethod

class CategoryOrder(ABC):
    @abstractmethod
    def __init__(self, *args):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
