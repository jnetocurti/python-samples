from src.oop.dog import Dog
from src.oop.wolf import Wolf


class DogWolf(Wolf, Dog):

    def activities(self):
        return super().activities() + Dog("").activities()
