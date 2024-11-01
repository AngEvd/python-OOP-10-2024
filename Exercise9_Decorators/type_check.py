from functools import wraps


def type_check(expected_type):

    def decorator(function):

        @wraps(function)
        def wrapper(arg):
            if isinstance(arg, expected_type):
                return function(arg)
            return "Bad Type"

        return wrapper

    return decorator
