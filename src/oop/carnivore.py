from src.oop.mammal import Mammal
from abc import abstractclassmethod, abstractmethod, abstractproperty


class Carnivore(Mammal):

    order = "Carnivore"

    @classmethod
    def of_order(cls):
        return cls.order
