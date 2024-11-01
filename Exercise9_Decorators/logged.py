from functools import wraps


def logged(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        name = function.__name__
        result = function(*args, **kwargs)
        return (f"you called {name}({', '.join(map(str, args))})"
                f"\nit returned {result}")
    return wrapper
