from itertools import permutations


def possible_permutations(elements):
    for result in permutations(elements):
        yield list(result)
