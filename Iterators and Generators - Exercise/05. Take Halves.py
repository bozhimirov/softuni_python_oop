def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    # TODO: Implement

    def halves():
        for i in integers():
            yield i / 2

    # TODO: Implement

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    # TODO: Implement

    return (take, halves, integers)

