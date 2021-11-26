import pytest
from src.design_patterns.factory import (
    Customer,
    Employee,
    SimpleFactoryUsers,
    XMLUserSerializeFactory,
    JsonUserSerializeFactory
)


class TestFactoryMethod:

    def test_create_employee_user(self):

        user = Employee.instance(
            login='dev@email.com',
            role='developer'
        )

        assert user.login == 'dev@email.com'
        assert user.role == 'developer'

    def test_create_customer_user(self):

        user = Customer.instance(
            login='customer@email.com',
            address='Guerrero no. 521, Pachuca de Soto, 42000'
        )

        assert user.login == 'customer@email.com'
        assert user.address == 'Guerrero no. 521, Pachuca de Soto, 42000'


class TestSimpleFactory:

    def test_create_employee_user(self):

        user = SimpleFactoryUsers.create_user(
            'employee',
            login='dev@email.com',
            role='developer'
        )

        assert isinstance(user, Employee)
        assert user.login == 'dev@email.com'
        assert user.role == 'developer'

    def test_create_customer_user(self):

        user = SimpleFactoryUsers.create_user(
            'customer',
            login='customer@email.com',
            address='Guerrero no. 521, Pachuca de Soto, 42000'
        )

        assert isinstance(user, Customer)
        assert user.login == 'customer@email.com'
        assert user.address == 'Guerrero no. 521, Pachuca de Soto, 42000'

    def test_create_user_unsupported_type(self):

        with pytest.raises(ValueError):
            SimpleFactoryUsers.create_user('whatever')


class TestAbstractFactory:

    def test_user_serialize(self):

        factories = [JsonUserSerializeFactory, XMLUserSerializeFactory]

        employee = Employee.instance(
            login='dev@email.com',
            role='developer'
        )

        json, xml = [f.employee_serialize(employee) for f in factories]

        assert json == '{"login": "dev@email.com", "role": "developer"}'
        assert xml == '<?xml version="1.0" encoding="UTF-8" ?><Employee><login type="str">dev@email.com</login><role type="str">developer</role></Employee>'  # noqa

        customer = Customer.instance(
            login='customer@email.com',
            address='Guerrero no. 521, Pachuca de Soto, 42000'
        )

        json, xml = [f.customer_serialize(customer) for f in factories]

        assert json == '{"login": "customer@email.com", "address": "Guerrero no. 521, Pachuca de Soto, 42000"}'  # noqa
        assert xml == '<?xml version="1.0" encoding="UTF-8" ?><Customer><login type="str">customer@email.com</login><address type="str">Guerrero no. 521, Pachuca de Soto, 42000</address></Customer>'  # noqa
