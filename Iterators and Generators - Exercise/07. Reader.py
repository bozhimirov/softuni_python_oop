def read_next(*args):
    for arg in args:
        for el in arg:
            yield el
