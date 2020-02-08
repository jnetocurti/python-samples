from abc import ABC, abstractstaticmethod, abstractclassmethod, \
    abstractmethod,  abstractproperty


class Animal(ABC):

    @abstractstaticmethod
    def of_class():
        pass

    @abstractclassmethod
    def of_order(cls):
        pass

    @abstractclassmethod
    def of_family(cls):
        pass

    @abstractproperty
    def specie(self):
        pass

    @abstractmethod
    def activities(self):
        pass

    def __str__(self):
        return f"Class: {self.of_class()}, Order: {self.of_order()}," + \
            f" Family: {self.of_family()}, Specie: {self.specie}"
