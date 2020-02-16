from src.oop.canids import Canids


class Wolf(Canids):

    def __init__(self):
        self._specie = "Canis lupus"
        self._activities = ('hunt', 'howl')

    @property
    def specie(self):
        return self._specie

    def activities(self):
        return self._activities

    def howl(self):
        return "OWOooooooooooooooooooo!"
