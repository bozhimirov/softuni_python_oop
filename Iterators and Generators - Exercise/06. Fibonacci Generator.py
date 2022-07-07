def fibonacci():
    first = 0
    second = 1
    yield first
    yield second

    while True:
        result = first + second
        first, second = second, result
        yield result
