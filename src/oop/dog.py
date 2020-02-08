from src.oop.canids import Canids
from abc import abstractclassmethod, abstractmethod, abstractproperty


class Dog(Canids):

    def __init__(self, name):
        self.__name = name
        self._specie = "Canis lupus familiaris"
        self._activities = ('play', 'bark')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def specie(self):
        return self._specie

    def activities(self):
        return self._activities

    def bark(self):
        return self.__bark()

    def __bark(self):
        return "Woof! Woof!"
