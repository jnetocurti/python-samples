from src.oop.animal import Animal
from abc import abstractclassmethod, abstractmethod, abstractproperty


class Mammal(Animal):

    @staticmethod
    def of_class():
        return "Mammal"
