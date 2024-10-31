from itertools import permutations


def possible_permutations(elements):
    for element in permutations(elements):
        yield list(element)

