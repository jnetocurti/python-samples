import json
from abc import ABC, abstractmethod, abstractstaticmethod

from dicttoxml import dicttoxml


class User(ABC):

    def __init__(self, login: str) -> None:
        self.__login = login

    def __eq__(self, o: object) -> bool:
        return o.__dict__() == self.__dict__()

    @property
    def login(self):
        return self.__login

    # factory method
    @abstractstaticmethod
    def instance(**kargs):
        pass


class Employee(User):

    def __init__(self, login: str, role: str) -> None:
        super().__init__(login)
        self.__role = role

    def __dict__(self):
        return {'login': self.login, 'role': self.role}

    @property
    def role(self):
        return self.__role

    # factory method
    @staticmethod
    def instance(**kargs):
        return Employee(**kargs)


class Customer(User):

    def __init__(self, login: str, address: str) -> None:
        super().__init__(login)
        self.__address = address

    def __dict__(self):
        return {'login': self.login, 'address': self.address}

    @property
    def address(self):
        return self.__address

    # factory method
    @staticmethod
    def instance(**kargs):
        return Customer(**kargs)


# Simple factory
class SimpleFactoryUsers:

    @staticmethod
    def create_user(type: str, **kwargs: dict) -> User:

        if type == 'employee':
            return Employee(**kwargs)

        elif type == 'customer':
            return Customer(**kwargs)

        else:
            raise ValueError('Unsupported user type')


class UserSerializer(ABC):

    @abstractmethod
    def serialize(self, user: User) -> str:
        pass


class JsonUserSerializer(UserSerializer):

    def serialize(self, user: User) -> str:
        return json.dumps(user.__dict__())


class XMLUserSerializer(UserSerializer):

    def serialize(self, user: User) -> str:
        custom_root = type(user).__name__
        return dicttoxml(user.__dict__(), custom_root=custom_root).decode()


# Abstract factory
class AbstractUserSerializeFactory(ABC):

    @abstractstaticmethod
    def employee_serialize(employee: Employee) -> str:
        pass

    @abstractstaticmethod
    def customer_serialize(customer: Customer) -> str:
        pass


# Abstract factory
class JsonUserSerializeFactory(AbstractUserSerializeFactory):

    @staticmethod
    def employee_serialize(employee: Employee) -> str:
        return JsonUserSerializer().serialize(employee)

    @staticmethod
    def customer_serialize(customer: Customer) -> str:
        return JsonUserSerializer().serialize(customer)


# Abstract factory
class XMLUserSerializeFactory(AbstractUserSerializeFactory):

    @staticmethod
    def employee_serialize(employee: Employee) -> str:
        return XMLUserSerializer().serialize(employee)

    @staticmethod
    def customer_serialize(customer: Customer) -> str:
        return XMLUserSerializer().serialize(customer)
