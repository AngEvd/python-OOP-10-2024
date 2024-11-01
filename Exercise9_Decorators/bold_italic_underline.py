from functools import wraps


def make_bold(function):

    @wraps(function)
    def wrapper(*args):
        text = function(*args)
        return f"<b>{text}</b>"

    return wrapper


def make_italic(function):

    @wraps(function)
    def wrapper(*args):
        text = function(*args)
        return f"<i>{text}</i>"

    return wrapper


def make_underline(function):

    @wraps(function)
    def wrapper(*args):
        text = function(*args)
        return f"<u>{text}</u>"

    return wrapper
