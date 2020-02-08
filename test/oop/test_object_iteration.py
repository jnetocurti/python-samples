import pytest
from src.oop.dog import Dog
from src.oop.pets import Pets


def get_pets():
    return Pets(Dog("Rex"), Dog("Lassie"), Dog("Beethoven"))


def test_next_objects_iteration():
    pets = get_pets()
    assert "Beethoven" == next(pets).name
    assert "Lassie" == next(pets).name
    assert "Rex" == next(pets).name


def test_loop_objects_iteration():
    pets = get_pets()
    assert ["Rex", "Lassie", "Beethoven"] == [p.name for p in pets]
