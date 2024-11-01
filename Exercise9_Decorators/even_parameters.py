from functools import wraps


def even_parameters(function):

    @wraps(function)
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int) or int(arg) % 2 != 0:
                return "Please use only even numbers!"
        return function(*args)

    return wrapper
