def even_numbers(function):

    def wrapper(numbers):
        even = [num for num in numbers if num % 2 == 0]
        return even

    return wrapper
