class reverse_iter:
    def __init__(self, values):
        self.values = values
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < -len(self.values):
            raise StopIteration

        value_to_return = self.values[self.index]
        self.index -= 1
        return value_to_return
