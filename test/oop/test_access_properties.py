import pytest
from src.oop.dog import Dog

dog = Dog("Rex")


def test_private_property_access():
    assert "Rex" == dog.name
    assert "Rex" == dog._Dog__name


def test_private_property_setter_access():
    dog.name = "Rex jr"
    assert "Rex jr" == dog.name

    dog._Dog__name = "Rex"
    assert "Rex" == dog.name


def test_private_method_access():
    with pytest.raises(
            AttributeError, match="'Dog' object has no attribute '__bark'"):
        dog.__bark()

    assert "Woof! Woof!" == dog._Dog__bark()
