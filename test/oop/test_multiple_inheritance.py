from src.oop.dogwolf import DogWolf, DogWolfMixin

dogWolf = DogWolf("Rex")
dogWolfMixin = DogWolfMixin("Lassie")


def test_multiple_inheritance():
    assert "Woof! Woof!" == dogWolf.bark()
    assert "OWOooooooooooooooooooo!" == dogWolf.howl()


def test_method_decision():
    assert 'Canis lupus familiaris' == dogWolf.specie


def test_overload_method():
    assert ('play', 'bark', 'hunt', 'howl') == dogWolf.activities()


def test_mixin_inheritance():
    assert ('play', 'bark', 'hunt', 'howl') == dogWolfMixin.activities()
