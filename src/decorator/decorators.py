from time import time


def log_passed_params(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        if args or kwargs:
            args = ','.join(str(a) for a in args)
            kwargs = ','.join(f"{k}={v}" for k, v in kwargs.items())
            print(f"passed params: {args}{(',' + kwargs) or ''}")

    return wrapper


class LogPassedParams:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)
        if args or kwargs:
            args = ','.join(str(a) for a in args)
            kwargs = ','.join(f"{k}={v}" for k, v in kwargs.items())
            print(f"passed params: {args}{(',' + kwargs) or ''}")


def log_time_execution(func):
    def wrapper(*args, **kwargs):
        init = time()
        func(*args, **kwargs)
        print(f"executed in : {round(time() - init, 4)} seconds")

    return wrapper


class LogTimeExecution():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        init = time()
        self.func(*args, **kwargs)
        print(f"executed in : {round(time() - init, 4)} seconds")


def params_modifier(func):
    def wrapper(**kargs):
        kargs.update({"user": "foo"})
        func(**kargs)

    return wrapper


class ParamsModifier():
    def __init__(self, func):
        self.func = func

    def __call__(self, **kwargs):
        kwargs.update({"user": "foo"})
        self.func(**kwargs)


def authorize(*roles):
    def decorator(func):
        def decorated(*args, **kwargs):
            if bool(set(roles).intersection(set((get_user_roles())))):
                return func(*args, **kwargs)
            raise Exception("permission denied")
        return decorated
    return decorator


class Authorize(object):
    def __init__(self, *roles):
        self.roles = roles

    def __call__(self, func, *args, **kwargs):
        def inner_func(*args, **kwargs):
            if bool(set(self.roles).intersection(set((get_user_roles())))):
                return func(*args, **kwargs)
            raise Exception("permission denied")

        return inner_func


# mock in tests
def get_user_roles():
    pass


def is_equals(Cls):
    class Decorator():
        def __init__(self, *args, **kwargs):
            self.decorated = Cls(*args, **kwargs)

        def is_equals(self, other):
            this, other = self.decorated, other.decorated
            if not isinstance(other, this.__class__):
                return False
            return id(self) == id(other) or this.__dict__ == other.__dict__

    return Decorator


def IsEquals(Cls):
    class Decorator():
        def __init__(self, *args, **kwargs):
            self.decorated = Cls(*args, **kwargs)

        def is_equals(self, other):
            this, other = self.decorated, other.decorated
            if not isinstance(other, this.__class__):
                return False
            return id(self) == id(other) or this.__dict__ == other.__dict__

    return Decorator
