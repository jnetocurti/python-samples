from src.oop.carnivore import Carnivore
from abc import abstractclassmethod, abstractmethod, abstractproperty


class Canids(Carnivore):

    family = "Canids"

    @classmethod
    def of_family(cls):
        return cls.family
