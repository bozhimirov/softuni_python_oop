class sequence_repeat:
    def __init__(self, text, number):
        self.text = text
        self.number = number
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.number:
            raise StopIteration
        result = self.text[self.idx % len(self.text)]
        self.idx += 1
        return result

