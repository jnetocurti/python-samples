from src.oop.canids import Canids
from abc import abstractclassmethod, abstractmethod, abstractproperty


class Wolf(Canids):

    def __init__(self):
        self._specie = "Canis lupus"

    @property
    def specie(self):
        return self._specie

    def activities(self):
        return ('hunt', 'howl')
