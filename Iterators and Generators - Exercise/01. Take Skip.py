class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.count:
            raise StopIteration
        result = self.iterations * self.step
        self.iterations += 1
        return result
