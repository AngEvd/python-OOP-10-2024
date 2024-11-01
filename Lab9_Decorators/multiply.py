def multiply(times):
    def decorator(function):
        def wrapper(num):
            return times * function(num)
        return wrapper
    return decorator
