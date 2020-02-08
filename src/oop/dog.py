from src.oop.canids import Canids
from abc import abstractclassmethod, abstractmethod, abstractproperty


class Dog(Canids):

    def __init__(self):
        self._specie = "Canis lupus familiaris"

    @property
    def specie(self):
        return self._specie

    def activities(self):
        return ('play', 'bark')
