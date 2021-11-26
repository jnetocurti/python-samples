import pytest
from src.oop.dog import Dog
from src.oop.wolf import Wolf
from src.oop.animal import Animal
from src.oop.canids import Canids
from src.oop.mammal import Mammal
from src.oop.carnivore import Carnivore


def test_can_not_instantiate_animal():
    with pytest.raises(
            TypeError,
            match="Can't instantiate abstract class Animal with abstract methods activities, of_class, of_family, of_order, specie"  # noqa
    ):
        _ = Animal()


def test_can_not_instantiate_mammal():
    with pytest.raises(
            TypeError,
            match="Can't instantiate abstract class Mammal with abstract methods activities, of_family, of_order, specie"  # noqa
    ):
        _ = Mammal()


def test_implemented_abstract_static_method():
    assert "Mammal" == Mammal.of_class()


def test_can_not_instantiate_carnivore():
    with pytest.raises(
            TypeError,
            match="Can't instantiate abstract class Carnivore with abstract methods activities, of_family, specie"  # noqa
    ):
        _ = Carnivore()


def test_can_not_instantiate_canids():
    with pytest.raises(
            TypeError,
            match="Can't instantiate abstract class Canids with abstract methods activities, specie"  # noqa
    ):
        _ = Canids()


def test_implemented_abstract_class_method():
    assert "Carnivore" == Carnivore.of_order()
    assert "Carnivore" == Wolf().of_order()
    assert "Canids" == Canids.of_family()
    assert "Canids" == Dog("Rex").of_family()


def test_can_instantiate_wolf():
    wolf = Wolf()
    assert wolf is not None
    assert "Class: Mammal, Order: Carnivore, Family: Canids, Specie: Canis lupus" == str(wolf)  # noqa?


def test_can_instantiate_dog():
    dog = Dog("Rex")
    assert dog is not None
    assert "Class: Mammal, Order: Carnivore, Family: Canids, Specie: Canis lupus familiaris" == str(dog)  # noqa?


def test_implemented_abstract_property():
    assert "Canis lupus" == Wolf().specie
    assert "Canis lupus familiaris" == Dog("Rex").specie


def test_implemented_abstract_method():
    assert ('play', 'bark') == Dog("Rex").activities()
    assert ('hunt', 'howl') == Wolf().activities()
