def vowel_filter(function):

    def wrapper():
        letters = function()
        return [char for char in letters if char.upper() in "AEIOUY"]

    return wrapper

