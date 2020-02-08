from src.oop.dog import Dog
from src.oop.wolf import Wolf


class DogWolf(Dog, Wolf):

    def activities(self):
        return super().activities() + Wolf().activities()


class WolfMixin():

    def activities(self):
        return self._activities + Wolf().activities()


class DogWolfMixin(WolfMixin, Dog):
    pass
