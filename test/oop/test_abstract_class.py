import pytest
from src.oop.animal import Animal
from src.oop.mammal import Mammal
from src.oop.carnivore import Carnivore
from src.oop.canids import Canids
from src.oop.wolf import Wolf
from src.oop.dog import Dog


def test_can_not_instantiate_animal():
    with pytest.raises(
            TypeError,
            match="Can't instantiate abstract class Animal with abstract"
        + " methods activities, of_class, of_family, of_order, specie"
    ):
        _ = Animal()


def test_can_not_instantiate_mammal():
    with pytest.raises(
            TypeError,
            match="Can't instantiate abstract class Mammal with abstract"
        + " methods activities, of_family, of_order, specie"
    ):
        _ = Mammal()


def test_implemented_abstract_static_method():
    assert "Mammal" == Mammal.of_class()


def test_can_not_instantiate_carnivore():
    with pytest.raises(
            TypeError,
            match="Can't instantiate abstract class Carnivore with abstract"
        + " methods activities, of_family, specie"
    ):
        _ = Carnivore()


def test_can_not_instantiate_canids():
    with pytest.raises(
            TypeError,
            match="Can't instantiate abstract class Canids with abstract"
        + " methods activities, specie"
    ):
        _ = Canids()


def test_implemented_abstract_class_method():
    assert "Carnivore" == Carnivore.of_order()
    assert "Carnivore" == Wolf().of_order()
    assert "Canids" == Canids.of_family()
    assert "Canids" == Dog().of_family()


def test_can_instantiate_wolf():
    wolf = Wolf()
    assert wolf is not None
    assert "Class: Mammal, Order: Carnivore, Family: Canids, Specie: Canis lupus" == str(wolf)  # noqa?


def test_can_instantiate_dog():
    dog = Dog()
    assert dog is not None
    assert "Class: Mammal, Order: Carnivore, Family: Canids, Specie: Canis lupus familiaris" == str(dog)  # noqa?


def test_implemented_abstract_property():
    assert "Canis lupus" == Wolf().specie
    assert "Canis lupus familiaris" == Dog().specie


def test_implemented_abstract_method():
    assert ('play', 'bark') == Dog().activities()
    assert ('hunt', 'howl') == Wolf().activities()
