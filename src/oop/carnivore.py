from src.oop.mammal import Mammal


class Carnivore(Mammal):

    order = "Carnivore"

    @classmethod
    def of_order(cls):
        return cls.order
