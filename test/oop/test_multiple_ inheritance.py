import pytest
from src.oop.dogwolf import DogWolf

dogWolf = DogWolf()


def test_multiple_inheritance():
    assert "Woof! Woof!" == dogWolf.bark()
    assert "OWOooooooooooooooooooo!" == dogWolf.howl()


def test_method_decision():
    assert 'Canis lupus' == dogWolf.specie


def test_overload_method():
    assert ('hunt', 'howl', 'play', 'bark') == dogWolf.activities()
