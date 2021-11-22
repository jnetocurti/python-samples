from src.design_patterns.singleton import (
    ModuleSingleton,
    DecoratedSingleton,
    SingletonSimpleImpl,
    SingletonMetaclassBased
)


class TestModuleSingleton:

    def test_module_singleton(self):
        from src.design_patterns.singleton import (
            ModuleSingleton as AnotherReference
        )

        assert id(ModuleSingleton) == id(AnotherReference)


class TestSingletonSimpleImpl:

    def test_singleton_simple_impl(self):
        reference_one = SingletonSimpleImpl()
        reference_two = SingletonSimpleImpl()

        assert id(reference_one) == id(reference_two)
        assert (reference_one.description ==
                "It's a simple singleton implementation")
        assert reference_one.description == reference_two.description


class TestSingletonMetaclassBased:

    def test_singleton_metaclass_based(self):
        reference_one = SingletonMetaclassBased()
        reference_two = SingletonMetaclassBased()

        assert id(reference_one) == id(reference_two)
        assert (reference_one.description ==
                "It's a singleton implementation based on metaclass")
        assert reference_one.description == reference_two.description


class TestDecoratedSingleton:

    def test_singleton_metaclass_based(self):
        reference_one = DecoratedSingleton()
        reference_two = DecoratedSingleton()

        assert id(reference_one) == id(reference_two)
        assert (reference_one.description ==
                "It's a decorated singleton implementation")
        assert reference_one.description == reference_two.description
