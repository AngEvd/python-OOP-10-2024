def tags(tag):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return f"<{tag}>{result}</{tag}>"

        return wrapper

    return decorator

