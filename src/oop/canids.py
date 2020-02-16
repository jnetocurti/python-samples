from src.oop.carnivore import Carnivore


class Canids(Carnivore):

    family = "Canids"

    @classmethod
    def of_family(cls):
        return cls.family
