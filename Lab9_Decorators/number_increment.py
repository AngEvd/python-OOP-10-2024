def number_increment(numbers):

    def increase():
        result = []
        for num in numbers:
            result.append(num + 1)
        return result

    return increase()
