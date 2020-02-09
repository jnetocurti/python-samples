import re
import pytest
from mock import patch
from io import StringIO
from src.decorator import decorators


@patch("sys.stdout", new_callable=StringIO)
def test_log_passed_params(mock_stdout):

    @decorators.log_passed_params
    def parameter_receiver(*args, **kwargs):
        pass

    parameter_receiver(1, 2, 3, param4=4, param5=5, param6=6)
    assert ("passed params: 1,2,3,param4=4,param5=5,param6=6\n" ==
            mock_stdout.getvalue())


@patch("sys.stdout", new_callable=StringIO)
def test_log_passed_params_class_version(mock_stdout):

    @decorators.LogPassedParams
    def parameter_receiver(*args, **kwargs):
        pass

    parameter_receiver(1, 2, 3, param4=4, param5=5, param6=6)
    assert ("passed params: 1,2,3,param4=4,param5=5,param6=6\n" ==
            mock_stdout.getvalue())


@patch("sys.stdout", new_callable=StringIO)
def test_log_time_execution(mock_stdout):

    @decorators.log_time_execution
    def iterate_range(start=0, end=10000000):
        for _ in range(start, end):
            pass

    log_pattern = re.compile(
        r"^executed in : \d*\.\d* seconds$")

    iterate_range()
    assert log_pattern.match(mock_stdout.getvalue())


@patch("sys.stdout", new_callable=StringIO)
def test_log_time_execution_class_version(mock_stdout):

    @decorators.LogTimeExecution
    def iterate_range(start=0, end=10000000):
        for _ in range(start, end):
            pass

    log_pattern = re.compile(
        r"^executed in : \d*\.\d* seconds$")

    iterate_range()
    assert log_pattern.match(mock_stdout.getvalue())


@patch("sys.stdout", new_callable=StringIO)
def test_params_modifier(mock_stdout):

    @decorators.params_modifier
    def parameter_receiver(**kwargs):
        print(kwargs)

    parameter_receiver(param1=1, param2=2)
    assert ("{'param1': 1, 'param2': 2, 'user': 'foo'}\n" ==
            mock_stdout.getvalue())


@patch("sys.stdout", new_callable=StringIO)
def test_params_modifier_class_version(mock_stdout):

    @decorators.ParamsModifier
    def parameter_receiver(**kwargs):
        print(kwargs)

    parameter_receiver(param1=1, param2=2)
    assert ("{'param1': 1, 'param2': 2, 'user': 'foo'}\n" ==
            mock_stdout.getvalue())


@patch('src.decorator.decorators.get_user_roles')
def test_authorize(get_user_roles_mock):
    get_user_roles_mock.return_value = ('user', 'admin', 'root')

    @decorators.authorize('user', 'admin')
    def do_something_authorized():
        pass

    assert None == do_something_authorized()

    @decorators.authorize('other')
    def do_something_not_authorized():
        pass

    with pytest.raises(Exception, match='permission denied'):
        do_something_not_authorized()


@patch('src.decorator.decorators.get_user_roles')
def test_authorize_class_version(get_user_roles_mock):
    get_user_roles_mock.return_value = ('user', 'admin', 'root')

    @decorators.Authorize('user', 'admin')
    def do_something_authorized():
        pass

    assert None == do_something_authorized()

    @decorators.Authorize('other')
    def do_something_not_authorized():
        pass

    with pytest.raises(Exception, match='permission denied'):
        do_something_not_authorized()


def test_class_is_equals_decorator():

    @decorators.is_equals
    class People():
        def __init__(self, name, age):
            self.name = name
            self.age = age

    a = People("Foo", 18)
    b = People("Foo", 18)
    c = People("Bar", 18)
    d = c

    assert a.is_equals(b)
    assert b.is_equals(a)
    assert c.is_equals(d)
    assert d.is_equals(c)
    assert not a.is_equals(c)


def test_class_is_equals_decorator_class_version():

    @decorators.IsEquals
    class People():
        def __init__(self, name, age):
            self.name = name
            self.age = age

    a = People("Foo", 18)
    b = People("Foo", 18)
    c = People("Bar", 18)
    d = c

    assert a.is_equals(b)
    assert b.is_equals(a)
    assert c.is_equals(d)
    assert d.is_equals(c)
    assert not a.is_equals(c)
