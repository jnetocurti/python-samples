

from typing import Any


class _ModuleSingleton:

    def __init__(self, description: str) -> None:
        self.__description = description

    @property
    def description(self) -> str:
        return self.__description


ModuleSingleton = _ModuleSingleton("It's a form of Singleton module")


class SingletonSimpleImpl:

    __instance = None

    def __new__(cls):

        if not cls.__instance:
            cls.__instance = super(SingletonSimpleImpl, cls).__new__(cls)

        return cls.__instance

    def __init__(self) -> None:
        self.__description = "It's a simple singleton implementation"

    @property
    def description(self) -> str:
        return self.__description


class MetaclassSingleton(type):

    __instances = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:

        if cls not in cls.__instances:
            cls.__instances[cls] = super(
                MetaclassSingleton, cls).__call__(cls, *args, **kwargs)

        return cls.__instances[cls]


class SingletonMetaclassBased(metaclass=MetaclassSingleton):

    def __init__(self, *args, **kwargs) -> None:
        self.__description = "It's a singleton implementation based on metaclass"  # noqa

    @property
    def description(self) -> str:
        return self.__description


class _SingletonWrapper:

    def __init__(self, cls):
        self._instance = None
        self.__wrapped__ = cls

    def __call__(self, *args, **kwargs):

        if self._instance is None:
            self._instance = self.__wrapped__(*args, **kwargs)

        return self._instance


def singleton(cls):
    return _SingletonWrapper(cls)


@singleton
class DecoratedSingleton:

    def __init__(self) -> None:
        self.__description = "It's a decorated singleton implementation"

    @property
    def description(self) -> str:
        return self.__description
